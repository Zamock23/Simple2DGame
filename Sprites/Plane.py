import arcade

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080


class Plane(arcade.Sprite):
    def __int__(self, texture):
        super().__init__(self)
        self.texture = texture
        self.scale = 0.2
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = SCREEN_HEIGHT // 2
        self.top = SCREEN_HEIGHT // 2 + 150
        self.left = SCREEN_WIDTH // 2 - 550
