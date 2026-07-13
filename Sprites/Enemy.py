import arcade, math

SPEED = 300


class Enemy(arcade.Sprite):
    def __int__(self, texture, scale, x, y, angle):
        super().__init__()

    def update(self, delta_time):
        an = math.radians(self.angle)
        dx = math.sin(an) * SPEED
        dy = math.cos(an) * SPEED

        self.center_x += dx * delta_time
        self.center_y += dy * delta_time
