"""
Mistery library
"a ghost tale"...
"""
"""
authors:
code: Fabian Ricardo Tobar Numesqui(frtobarn@unal.edu.co)
concept-art: Maria Camila Diaz Guevara
"""

# Importing arcade library
import arcade

# Importing classes
from config import Config
from presentation_view import PresentationView

# Executing custom configurations
config = Config()  # singleton


# Main class
class MisteryLibraryGame(arcade.Window):
    def __init__(
        self,
        width: int = config.screen_width,
        height: int = config.screen_height,
        title: str | None = "Mistery Library",
        fullscreen: bool = True,
        update_rate: float | None = 1 / 30,
    ):
        super().__init__(width, height, title, fullscreen, update_rate)

        # Setting up window location
        self.set_location(0, 0)
        arcade.set_background_color(arcade.color.BLACK)

        # Don't show the mouse cursor
        self.set_mouse_visible(False)


if __name__ == "__main__":
    # main
    window = MisteryLibraryGame(
        config.screen_width, config.screen_height, "Mistery Library"
    )
    window.total_score = 100
    presentation_view = PresentationView()
    window.show_view(presentation_view)
    arcade.run()
