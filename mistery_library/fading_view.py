import arcade

from config import Config

config = Config()

WIDTH = 800
HEIGHT = 600

FADE_RATE = 5


class FadingView(arcade.View):
    def __init__(self):
        super().__init__()
        self.fade_out = None
        self.fade_in = 255

    def update_fade(self, next_view=None):
        if self.fade_out is not None:
            self.fade_out += FADE_RATE
            if (
                self.fade_out is not None
                and self.fade_out > 255
                and next_view is not None
            ):
                game_view = next_view()
                game_view.setup()
                self.window.show_view(game_view)

        if self.fade_in is not None:
            self.fade_in -= FADE_RATE
            if self.fade_in <= 0:
                self.fade_in = None

    def draw_fading(self):
        if self.fade_out is not None:
            arcade.draw_rectangle_filled(
                arcade.get_viewport()[0] + config.screen_half_width,
                arcade.get_viewport()[2] + config.screen_half_height,
                config.screen_width,
                config.screen_height,
                (0, 0, 0, self.fade_out),
            )

        if self.fade_in is not None:
            arcade.draw_rectangle_filled(
                arcade.get_viewport()[0] + config.screen_half_width,
                arcade.get_viewport()[2] + config.screen_half_height,
                config.screen_width,
                config.screen_height,
                (0, 0, 0, self.fade_in),
            )
