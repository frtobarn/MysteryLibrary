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

# Importing os library
import os


# Importing classes
from config import Config
from player import Player
from ghost import Ghost
from map import Map

# Executing custom configurations
# singleton
config = Config()


# Physics
MOVEMENT_SPEED = 8
JUMP_SPEED = 28
GRAVITY = 0


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
        arcade.set_background_color(arcade.color.BLUE_GRAY)

        # creating a level or map
        self.map_1 = Map("map_01")

        # Creating a player and some ghosts
        self.player = Player(
            "Player", config.screen_width // 2, config.screen_height // 2, 100
        )
        self.ghost_1 = Ghost("ghost_1", 100, 150, 0.001, "", "")

        # Physics
        self.physics_engine = None

        # introducing score
        self.score = 0

        # Running setup fuction
        self.setup()

    def setup(self):
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player.character_sprite,
            self.map_1.scene.get_sprite_list("Terrain"),
            gravity_constant=GRAVITY,
        )

    # Called once a frame to render the window
    def on_draw(self):
        """Render the screen."""
        # Clear the screen to load the background color
        self.clear()

        # Gets the setup to render
        arcade.start_render()

        # Drawing tiled map
        self.map_1.draw()

        # Drawing player's  and ghost's animated sprite
        self.player.draw()
        self.ghost_1.draw()

        # Drawing optinos on screen
        self.draw_info()

    # On_update function(called every frame)
    def on_update(self, delta_time: float):
        # Updating physics engine
        self.physics_engine.update()
        # updating player's animated sprite list
        self.player.update()
        # Executing ghost's logic
        self.ghost_1.update(delta_time)

    # Setting up input keys
    def on_key_press(self, symbol: int, modifiers: int):
        # inputs for player
        self.player.on_key_press(symbol, modifiers)

    def on_key_release(self, symbol: int, modifiers: int):
        # Inputs for player
        self.player.on_key_release(symbol, modifiers)

    # Setting up mouse follow

    # Getting inputs from mouse
    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.player.on_mouse_motion(x, y)

    # Inputs for light mouse's buttons
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        self.player.light.on_mouse_press(x, y, button, modifiers)

    # drawing interface
    def draw_info(self):
        # Drawing a frame
        arcade.draw_lines(
            [
                (0, 0),
                (config.screen_width, 0),
                (config.screen_width, 0),
                (config.screen_width, config.screen_height),
                (config.screen_width, config.screen_height),
                (0, config.screen_height),
                (0, config.screen_height),
                (0, 0),
            ],
            arcade.color.ALABAMA_CRIMSON,
            10,
        )
        # Drawing score text
        arcade.draw_text(
            f"Score: {self.score}",
            arcade.get_viewport()[0] + 10,
            arcade.get_viewport()[2] + config.screen_height - 30,
            arcade.color.GOLD,
            font_size=20,
        )


# Creating my window
MisteryLibraryGame(config.screen_width, config.screen_height, "Mistery Library")
arcade.run()
