import arcade

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080


class Plane(arcade.Sprite):
    def __int__(self, texture, scale, x, y):
        super().__init__(self)
        self.texture = texture
        self.scale = scale
        self.center_x = x
        self.center_y = y
