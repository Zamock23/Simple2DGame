from random import randint, choice
import arcade

from pyglet.graphics import Batch

from Sprites.Plane import Plane
from Sprites.Enemy import Enemy

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN_TITLE = "Game"

BACKGROUND_TEXTURE = arcade.load_texture("Pictures/texture_to_view.png")

max_score = 0


def update_max_score():
    global max_score
    with open('best_score.txt', 'r', encoding='utf-8') as f:
        max_score = int(f.read())


class GameMenu(arcade.View):
    def __init__(self, score):
        super().__init__()
        self.batch = Batch()

        update_max_score()

        global max_score
        if score > max_score:
            max_score = score
            with open('best_score.txt', 'w', encoding='utf-8') as f:
                f.write(f'{max_score}')

        self.plane_number = 1

        self.button_list = arcade.SpriteList()

        self.start_btn = arcade.Sprite('Pictures/start_btn.png', 0.45)
        self.start_btn.center_x = SCREEN_WIDTH // 2
        self.start_btn.center_y = SCREEN_HEIGHT // 2
        self.start_btn.top = SCREEN_HEIGHT // 2 - 125
        self.start_btn.left = SCREEN_WIDTH // 2 - 375

        self.button_list.append(self.start_btn)

        self.change_btn_right = arcade.Sprite('Pictures/change_btn.png', 0.2, SCREEN_WIDTH // 2 + 130,
                                              SCREEN_HEIGHT // 2 + 100)
        self.change_btn_left = arcade.Sprite('Pictures/change_btn.png', 0.2, SCREEN_WIDTH // 2 - 525,
                                             SCREEN_HEIGHT // 2 + 100, 180)

        self.button_list.append(self.change_btn_right)
        self.button_list.append(self.change_btn_left)

        self.plane_list = arcade.SpriteList()
        self.plane_list.append(
            arcade.Sprite('Pictures/1plane.png', 0.6, SCREEN_WIDTH // 2 - 175, SCREEN_HEIGHT // 2 + 125))
        self.plane_list.append(
            arcade.Sprite('Pictures/2plane.png', 0.6, SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 + 150))

    def on_draw(self):
        self.clear()

        rect = arcade.rect.LRBT(0, 1920, 0, 1080)
        arcade.draw_texture_rect(BACKGROUND_TEXTURE, rect)

        self.button_list.draw()

        arcade.draw_sprite(self.plane_list[self.plane_number - 1])

        best_score = arcade.Text(f'Лучший результат: {max_score}', SCREEN_WIDTH // 2 - 175, SCREEN_HEIGHT - 50,
                                 font_size=60, anchor_x='center', anchor_y='center', bold=True,
                                 color=arcade.color.BLACK, batch=self.batch)
        self.batch.draw()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        change_plane_plus = arcade.get_sprites_at_point((x, y), self.button_list)
        if self.button_list[1] in change_plane_plus and self.plane_number < len(self.plane_list):
            self.plane_number += 1

        change_plane_minus = arcade.get_sprites_at_point((x, y), self.button_list)
        if self.button_list[2] in change_plane_minus and self.plane_number > 1:
            self.plane_number -= 1

        start_gaming = arcade.get_sprites_at_point((x, y), self.button_list)

        if self.button_list[0] in start_gaming:
            gaming = Gaming(self.plane_number)
            self.window.show_view(gaming)


class Gaming(arcade.View):
    def __init__(self, plane_num):
        super().__init__()
        self.batch = Batch()

        self.keys_pressed = set()
        self.spawn_enemy_timer = 0

        self.is_lose = False

        self.score = 0

        self.point = self.new_point()

        self.score_list = arcade.SpriteList()
        self.plane_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()

        self.score_list.append(self.point)

        self.plane = Plane(plane_num=plane_num)
        self.plane_list.append(self.plane)

    def new_point(self):
        return arcade.Sprite('Pictures/scoreSprite.png', 0.5, randint(50, SCREEN_WIDTH - 420),
                             randint(275, SCREEN_HEIGHT - 50))

    def spawn_enemy(self):
        side = choice([0, SCREEN_HEIGHT])
        ans = 0
        if side == SCREEN_HEIGHT:
            a, b = 100, 250
            ans = randint(a, b)
        else:
            a, b = randint(280, 360), randint(0, 70)
            ans = choice([a, b])
        enemy = Enemy('Pictures/enemy.png', 0.15, randint(0, SCREEN_WIDTH),
                      side, ans)
        self.enemy_list.append(enemy)

    def on_draw(self):
        self.clear()
        rect = arcade.rect.LRBT(0, 1920, 0, 1080)
        arcade.draw_texture_rect(BACKGROUND_TEXTURE, rect)
        self.plane_list.draw()
        self.enemy_list.draw()
        self.score_list.draw()

        score = arcade.Text(f'{self.score}', SCREEN_WIDTH - 400, SCREEN_HEIGHT - 50, font_size=40, anchor_x='right',
                            color=arcade.color.BLACK, bold=True, batch=self.batch)

        if self.is_lose:
            losing = arcade.Text(f'Ты врезался. Твой счёт {self.score}', SCREEN_WIDTH // 2 - 200,
                                 SCREEN_HEIGHT // 2 + 300,
                                 font_size=50, anchor_x='center', anchor_y='center',
                                 color=arcade.color.BLACK_LEATHER_JACKET, bold=True, batch=self.batch)
            inf_continue = arcade.Text('press space for continue', SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2,
                                       font_size=30, anchor_x='center', anchor_y='center', color=arcade.color.GRAY,
                                       batch=self.batch)

        self.batch.draw()

    def on_update(self, delta_time):
        if self.is_lose:
            return
        self.plane_list.update(delta_time, self.keys_pressed)
        self.spawn_enemy_timer += delta_time
        if self.spawn_enemy_timer >= 3:
            self.spawn_enemy_timer = 0
            self.spawn_enemy()

        self.enemy_list.update(delta_time)

        for enemy in self.enemy_list:
            x, y = enemy.center_x, enemy.center_y
            if x - 500 >= SCREEN_WIDTH or x + 500 <= 0:
                self.enemy_list.remove(enemy)
            elif y - 500 >= SCREEN_HEIGHT or y + 500 <= 0:
                self.enemy_list.remove(enemy)

        if arcade.check_for_collision(self.point, self.plane):
            self.score += 1
            self.score_list.remove(self.point)
            self.point = self.new_point()
            self.score_list.append(self.point)

        crash = arcade.check_for_collision_with_list(self.plane, self.enemy_list)
        for enemy in crash:
            self.is_lose = True
            break

    def on_key_press(self, key, modifiers):
        self.keys_pressed.add(key)
        if self.is_lose and key == arcade.key.SPACE:
            self.is_lose = False
            menu = GameMenu(self.score)
            self.window.show_view(menu)

    def on_key_release(self, key, modifiers):
        if key in self.keys_pressed:
            self.keys_pressed.remove(key)
