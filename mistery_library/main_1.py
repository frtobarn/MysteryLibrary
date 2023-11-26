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
GRAVITY = 0.0


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

        # creating a level or map
        self.level_1 = Map("level_1")

        # Creating a player and some ghosts
        start_pos = (config.screen_width // 2, config.screen_height // 2)
        self.player = Player("player", start_pos[0], start_pos[1], 100)

        # Creating some ghosts
        self.ghost_1 = Ghost("ghost_1", 100, 150, 0.001, "", "")
        self.ghost_2 = Ghost("ghost_2", 200, 250, 0.001, "", "")
        self.ghost_3 = Ghost("ghost_3", 300, 350, 0.001, "", "")
        self.ghost_4 = Ghost("ghost_4", 400, 450, 0.001, "", "")
        self.ghost_5 = Ghost("ghost_5", 500, 550, 0.001, "", "")

        # Physics
        self.physics_engine = None

        # introducing score
        self.score = 0

        # Running setup fuction
        self.setup()

    def setup(self):
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player.character_sprite,
            self.level_1.scene.get_sprite_list("walls"),
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
        self.level_1.draw()

        # Drawing player's  and ghost's animated sprite
        self.player.draw()
        self.ghost_1.draw()
        self.ghost_2.draw()
        self.ghost_3.draw()
        self.ghost_4.draw()
        self.ghost_5.draw()

        # Drawing optinos on screen
        self.draw_info()

    # On_update function(called every frame)
    def on_update(self, delta_time: float):
        # Updating physics engine
        self.physics_engine.update()
        # updating player's animated sprite list
        self.player.update()

        # moving camera
        self.move_camera()

        # Executing ghost's logic
        self.ghost_1.update(delta_time)
        self.ghost_2.update(delta_time)
        self.ghost_3.update(delta_time)
        self.ghost_4.update(delta_time)
        self.ghost_5.update(delta_time)

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

    # Claculating camera movement
    def clamp(self, value, mini, maxi):
        return max(min(value, maxi), mini)

    # moving camera
    def move_camera(self):
        # moving camera
        self.player.character_sprite.center_x = self.clamp(
            self.player.character_sprite.center_x, 0, self.level_1.width
        )

        self.player.character_sprite.center_y = self.clamp(
            self.player.character_sprite.center_y, 0, self.level_1.height
        )

        if (
            self.player.character_sprite.center_x > config.screen_half_width
            and self.player.character_sprite.center_x
            < self.level_1.width - self.level_1.tile_width - config.screen_half_width
            or self.player.character_sprite.center_y > config.screen_half_height
            and self.player.character_sprite.center_y
            < self.level_1.height - self.level_1.tile_height - config.screen_half_height
        ):
            change_view = True
        else:
            change_view = False

        if change_view:
            arcade.set_viewport(
                self.player.character_sprite.center_x - config.screen_half_width,
                self.player.character_sprite.center_x + config.screen_half_width,
                self.player.character_sprite.center_y - config.screen_half_height,
                self.player.character_sprite.center_y + config.screen_half_height,
            )

    def move_camera1(self):
        # moving camera
        self.player.character_sprite.center_x = self.clamp(
            self.player.character_sprite.center_x, 0, self.level_1.width
        )

        if (
            self.player.character_sprite.center_x > config.screen_half_width
            and self.player.character_sprite.center_x
            < self.level_1.width - self.level_1.tile_width - config.screen_half_width
        ):
            change_view = True
        else:
            change_view = False

        if change_view:
            arcade.set_viewport(
                self.player.character_sprite.center_x - config.screen_half_width,
                self.player.character_sprite.center_x + config.screen_half_width,
                0,
                config.screen_height,
            )

    # drawing interface
    def draw_info(self):
        # return
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
