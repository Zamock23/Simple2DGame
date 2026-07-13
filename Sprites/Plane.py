import arcade, math, csv

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080


class Plane(arcade.Sprite):
    def __int__(self, plane_num):
        super().__int__()

        with open('planes.csv', 'r', encoding='utf-8') as data:
            plane_data = list(csv.reader(data, delimiter=';'))[plane_num]
            texture = plane_data[1]
            speed = int(plane_data[2])

        self.speed = speed

        self.idle_texture = arcade.texture.load_texture(f"Pictures/{texture}")
        self.texture = self.idle_texture

        self.center_x, self.center_y = SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 150
        self.angle = 0
        self.scale = 0.2

    def update(self, delta_time, keys_pressed):
        dx, dy = 0, 0
        if arcade.key.UP in keys_pressed:
            an = math.radians(self.angle)
            dx = math.sin(an) * self.speed
            dy = math.cos(an) * self.speed
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
