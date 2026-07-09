import arcade

from Sprites.Plane import Plane
from Sprites.buttons import StartButton

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN_TITLE = "Game"

BACKGROUND_TEXTURE = arcade.load_texture("Pictures/texture_to_view.png")


class GameMenu(arcade.View):
    def __init__(self):
        super().__init__()

        self.start_btn = StartButton('Pictures/start_btn.png')

        self.button_list = arcade.SpriteList()
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

        self.plane = Plane('Pictures/plane.png')

        self.plane_list = arcade.SpriteList()
        self.plane_list.append(self.plane)

    def on_draw(self):
        self.clear()
        rect = arcade.rect.LRBT(0, 1920, 0, 1080)
        arcade.draw_texture_rect(BACKGROUND_TEXTURE, rect)
        self.plane_list.draw()
