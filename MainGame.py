from random import randint, choice
import arcade

from Sprites.Plane import Plane
from Sprites.Enemy import Enemy

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN_TITLE = "Game"

BACKGROUND_TEXTURE = arcade.load_texture("Pictures/texture_to_view.png")


class GameMenu(arcade.View):
    def __init__(self):
        super().__init__()

        self.button_list = arcade.SpriteList()

        self.start_btn = arcade.Sprite('Pictures/start_btn.png', 0.45)
        self.start_btn.center_x = SCREEN_WIDTH // 2
        self.start_btn.center_y = SCREEN_HEIGHT // 2
        self.start_btn.top = SCREEN_HEIGHT // 2 - 125
        self.start_btn.left = SCREEN_WIDTH // 2 - 375

        self.button_list.append(self.start_btn)

    def on_draw(self):
        self.clear()

        rect = arcade.rect.LRBT(0, 1920, 0, 1080)
        arcade.draw_texture_rect(BACKGROUND_TEXTURE, rect)

        self.button_list.draw()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        start_gaming = arcade.get_sprites_at_point((x, y), self.button_list)

        if self.button_list[0] in start_gaming:
            gaming = Gaming()
            self.window.show_view(gaming)


class Gaming(arcade.View):
    def __init__(self):
        super().__init__()
        self.keys_pressed = set()
        self.spawn_enemy_timer = 0

        self.plane_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()

        self.plane = Plane('Pictures/plane.png', 0.2, SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 150, 0)
        self.plane_list.append(self.plane)

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

    def on_update(self, delta_time):
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

    def on_key_press(self, key, modifiers):
        self.keys_pressed.add(key)

    def on_key_release(self, key, modifiers):
        if key in self.keys_pressed:
            self.keys_pressed.remove(key)
