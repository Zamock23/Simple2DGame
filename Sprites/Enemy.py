from random import randint

import arcade, math

SPEED = 300


class Enemy(arcade.Sprite):
    def __int__(self, texture, scale, x, y, angle):
        super().__init__(self)
        self.texture = texture
        self.scale = scale
        self.center_x = x
        self.center_y = y
        self.angle = angle

    def update(self, delta_time):
        an = math.radians(self.angle)
        dx = math.sin(an) * SPEED
        dy = math.cos(an) * SPEED

        self.center_x += dx * delta_time
        self.center_y += dy * delta_time
