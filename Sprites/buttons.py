import arcade

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080


class StartButton(arcade.Sprite):
    def __int__(self):
        super().__init__('Pictures/start_btn.png', 1.0)
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = SCREEN_HEIGHT // 2
