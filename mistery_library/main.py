"""
Mistery library
"a ghost tale"...
"""
"""
authors:
Fabian Ricardo Tobar Numesqui(frtobarn@unal.edu.co)
Maria Camila Diaz Guevara
"""

# Importing arcade library
import arcade

# Importing os library
import os


# Importing classes
from player import Player
from ghost import Ghost
from map import Map
from light import Light

# from math import sqrt # may be i need it later ;)

# Getting absolute path because im into a linux virtual environment
PATH = os.path.dirname(os.path.abspath(__file__)) + "/"
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


# Main class
class MyGameWindow(arcade.Window):
    def __init__(
        self,
        width: int = SCREEN_WIDTH,
        height: int = SCREEN_HEIGHT,
        title: str | None = "Mistery Library",
        fullscreen: bool = True,
        update_rate: float | None = 1 / 30,
    ):
        """,
        resizable: bool = True,
        update_rate: float | None = 1 / 60,
        antialiasing: bool = True,
        gl_version: Tuple[int, int] = ...,
        screen: XlibScreen = None,
        style: str | None = pyglet.window.Window.WINDOW_STYLE_DEFAULT,
        visible: bool = True,
        vsync: bool = False,
        gc_mode: str = "context_gc",
        center_window: bool = False,
        samples: int = 4,
        enable_polling: bool = True,"""
        super().__init__(width, height, title, fullscreen, update_rate)
        """,
        resizable,
        update_rate,
        antialiasing,
        gl_version,
        screen,
        style,
        visible,
        vsync,
        gc_mode,
        center_window,
        samples,
        enable_polling,"""

        # Setting up window location
        self.set_location(0, 0)
        arcade.set_background_color(arcade.color.BLUE_GRAY)

        # print(arcade.get_projection())

        # creating a level or map
        self.map_1 = Map("map_01")

        # Creating a player and some ghosts
        self.player = Player("Player", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 100, "")
        self.ghost_1 = Ghost("ghost_1", 100, 100, 1, "", "", "")

        # Position var for circle
        self.c_x = 150
        self.c_y = 50
        self.c_ang = 0

        # Speed vars for circle
        self.c_x_speed = 300
        self.c_y_speed = 100
        self.c_ang_speed = 0

    # called once a frame to render the window
    def on_draw(self):
        """Render the screen."""

        # Clear the screen to the background color
        self.clear()

        # Gets the setup to render
        arcade.start_render()

        # Drawing tiled map
        self.map_1.draw()

        # Drawing player's  and ghost's animated sprite
        self.player.draw()
        self.ghost_1.draw()

        # Drawing examples
        arcade.draw_lines([(0, 0), (100, 100)], arcade.color.ALABAMA_CRIMSON, 4)
        arcade.draw_point(105, 105, arcade.color.WINDSOR_TAN, 10)

        arcade.draw_circle_filled(
            self.c_x, self.c_y, 25, arcade.color.AMARANTH, self.c_ang, 10
        )

    # On_update function(called every frame)
    def on_update(self, delta_time: float):
        # Moving the filled circle
        self.c_x += self.c_x_speed * delta_time
        self.c_y += self.c_y_speed * delta_time
        self.c_ang += self.c_ang_speed * delta_time

        # Detecting outbounds
        if self.c_x + 30 > 1280 or self.c_x - 30 < 0:
            self.c_x_speed *= -1
            self.c_ang_speed *= -1
        if self.c_y + 30 > 720 or self.c_y - 30 < 0:
            self.c_y_speed *= -1
            self.c_ang_speed *= -1

        # Executing movement-inputs for player
        self.player.move()

        self.ghost_1.update()

        # self.player_sprite.set_position(self.player_x, self.player_y)
        # self.player_sprite.update()

        # update plater's animated sprite list
        self.player.update()

    # Setting up input keys
    def on_key_press(self, symbol: int, modifiers: int):
        # inputs for player
        self.player.on_key_press(symbol, modifiers)

    def on_key_release(self, symbol: int, modifiers: int):
        # Inputs for player
        self.player.on_key_release(symbol, modifiers)

    # Setting up mouse follow
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.c_x = x
            self.c_y = y
            self.c_x_speed *= -1
            self.c_y_speed *= -1

        if button == arcade.MOUSE_BUTTON_RIGHT:
            # self.rectangle_x = x
            # self.rectangle_y = y
            pass

    # Getting inputs from mouse
    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.player.on_mouse_motion(x, y)


# Creating my window
MyGameWindow(1280, 720, "Mistery Library")
arcade.run()
