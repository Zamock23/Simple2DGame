import arcade
from pyglet.graphics import Batch

from MainGame import GameMenu, BACKGROUND_TEXTURE

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN_TITLE = "Game"


class Start_View(arcade.View):
    def __init__(self):
        super().__init__()
        self.batch = Batch()

        self.sprite = arcade.Sprite("Pictures/plane.png", 0.5)
        self.sprite.center_y, self.sprite.center_x = SCREEN_HEIGHT // 2 - 100, SCREEN_WIDTH // 2 + 200
        self.sprite.angle = 27
        self.sprite.scale = 0.65

        self.sprite_list = arcade.SpriteList()
        self.sprite_list.append(self.sprite)

    def on_draw(self):
        self.clear()
        x, y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
        rect = arcade.rect.XYWH(x - 300, y, 1800, 1300)
        arcade.draw_texture_rect(BACKGROUND_TEXTURE, rect)

        name_game = arcade.Text("Try To Fly",
                                SCREEN_WIDTH // 2 - 500, SCREEN_HEIGHT // 2 + 200,
                                font_size=85, anchor_x="center", bold=True,
                                color=arcade.color.RED, batch=self.batch)

        start_message = arcade.Text("Space key for continue",
                                    SCREEN_WIDTH / 2 - 500, SCREEN_HEIGHT // 2 + 100,
                                    arcade.color.BLACK_LEATHER_JACKET, font_size=40, anchor_x="center",
                                    batch=self.batch)
        self.batch.draw()
        self.sprite_list.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            mainGame = GameMenu()
            self.window.show_view(mainGame)


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = Start_View()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()
