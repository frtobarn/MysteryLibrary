import arcade
from game_view import GameView
from config import Config
from fading_view import FadingView

config = Config()


class MenuView(FadingView):
    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_update(self, dt):
        self.update_fade(next_view=GameView)

    def on_draw(self):
        self.clear()
        arcade.draw_text(
            "Mistery library - space to advance",
            config.screen_half_width,
            config.screen_half_height,
            arcade.color.WHITE,
            font_size=30,
            anchor_x="center",
        )
        self.draw_fading()

    def on_key_press(self, key, _modifiers):
        # handling fading
        if self.fade_out is None and key == arcade.key.SPACE:
            self.fade_out = 0

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)"""
        pass
