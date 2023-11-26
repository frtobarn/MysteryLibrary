import arcade

from fading_view import FadingView
from config import Config


# from menu_view import MenuView
config = Config()


# inherit from FdingView to use transition
class GameOverView(FadingView):
    def __init__(self):
        super().__init__()
        self.score = 1

    def setup(self):
        pass

    def on_show_view(self):
        """Called when switching to this view"""
        arcade.set_background_color(arcade.color.BLACK)

    def on_update(self, dt):
        self.update_fade(next_view=None)

    def on_draw(self):
        """Draw the game over view"""
        self.clear()
        arcade.draw_text(
            "Game Over",
            arcade.get_viewport()[0] + 240,
            arcade.get_viewport()[2] + 400,
            arcade.color.WHITE,
            54,
        )
        arcade.draw_text(
            "Press any to exit",
            arcade.get_viewport()[0] + 310,
            arcade.get_viewport()[2] + 300,
            arcade.color.WHITE,
            24,
        )

        # score_formatted = f"{round(self.score, 2)} "
        arcade.draw_text(
            f"Score: {self.score}",
            arcade.get_viewport()[0] + config.screen_half_width,
            arcade.get_viewport()[2] + 200,
            arcade.color.WHITE,
            font_size=15,
            anchor_x="center",
        )

        output_total = f"Total Score: {self.window.total_score}"
        arcade.draw_text(
            output_total,
            arcade.get_viewport()[0] + 10,
            arcade.get_viewport()[2] + 10,
            arcade.color.WHITE,
            14,
        )

        self.draw_fading()

    def on_key_press(self, key, _modifiers):
        self.fade_out = 0
        arcade.Window.close(self.window)
