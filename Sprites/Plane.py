import arcade, math

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SPEED = 150


class Plane(arcade.Sprite):
    def __int__(self, texture, scale, x, y, angle):
        super().__init__(self)
        self.texture = texture
        self.scale = scale
        self.center_x = x
        self.center_y = y
        self.angle = angle

    def update(self, delta_time, keys_pressed):
        dx, dy = 0, 0
        if arcade.key.UP in keys_pressed:
            an = math.radians(self.angle)
            dx = math.sin(an) * SPEED
            dy = math.cos(an) * SPEED
        if arcade.key.RIGHT in keys_pressed:
            self.angle += 3
        if arcade.key.LEFT in keys_pressed:
            self.angle -= 3

        self.center_x += dx * delta_time
        self.center_y += dy * delta_time

        if self.center_x + 475 >= SCREEN_WIDTH:
            self.center_x = SCREEN_WIDTH - 475
        if self.center_x - 100 <= 0:
            self.center_x = 100
        if self.center_y + 80 >= SCREEN_HEIGHT:
            self.center_y = SCREEN_HEIGHT - 80
        if self.center_y - 320 <= 0:
            self.center_y = 320
