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
from clue import Clue

# from math import sqrt # may be i need it later ;)

# Getting absolute path because im into a linux virtual environment
PATH = os.path.dirname(os.path.abspath(__file__)) + "/"


# Main class
class MyGameWindow(arcade.Window):
    def __init__(
        self,
        width: int = 1280,
        height: int = 720,
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
        self.player = Player("Player", 1280 / 2, 720 / 2, 100, "")
        self.ghost_1 = Ghost("ghost_1", 100, 100, 1, "", "", "")

        # Creating clues
        self.clue_1 = Clue("clue_1", 900, 600, "")
        self.clue_2 = Clue("clue_2", 300, 300, "")

        # Using spritelist
        self.clue_list = arcade.SpriteList()
        self.clue_list.append(self.clue_1.clue_sprite)
        self.clue_list.append(self.clue_2.clue_sprite)

        # Position var for circle
        self.c_x = 150
        self.c_y = 50
        self.c_ang = 0

        # Speed vars for circle
        self.c_x_speed = 300
        self.c_y_speed = 100
        self.c_ang_speed = 0

        # Position var for rectangle
        self.rectangle_x = 150
        self.rectangle_y = 50
        self.rectangle_ang = 0

        # Speed vasr for rectangle
        self.rectangle_x_speed = 100
        self.rectangle_y_speed = 100
        self.rectangle_ang_speed = 0

        # Booleans for rectangle's movement
        self.rectangle_right = False
        self.rectangle_left = False
        self.rectangle_up = False
        self.rectangle_down = False

        # Custom cursor
        self.co_x = 150
        self.co_y = 50
        self.co_x_speed = 0
        self.co_y_speed = 0

        # Run animated sprite setup function
        # self.setup()

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

        # Drawing a sprite
        self.clue_list.draw()
        """
        self.player_sprite.draw()
        self.coin_sprite.draw()
        self.box_sprite.draw()
        """

        # Drawing examples
        arcade.draw_lines([(0, 0), (100, 100)], arcade.color.ALABAMA_CRIMSON, 4)
        arcade.draw_point(105, 105, arcade.color.WINDSOR_TAN, 10)
        arcade.draw_circle_filled(
            self.c_x, self.c_y, 25, arcade.color.AMARANTH, self.c_ang, 10
        )
        arcade.draw_circle_outline(
            self.co_x, self.co_y, 30, arcade.color.APRICOT, 3, 0, 10
        )
        arcade.draw_lrtb_rectangle_filled(
            self.rectangle_x,
            self.rectangle_x + 100,
            self.rectangle_y + 50,
            self.rectangle_y,
            arcade.color.AMAZON,
        )

        # return super().on_draw()

    def on_update(self, delta_time: float):
        # Moving cursor through mouse
        self.move_cursor()

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
        self.clue_list.update()

        # update plater's animated sprite list
        self.player.update()

        # Detenting inputs for rectangle
        if self.rectangle_right:
            self.rectangle_x += self.rectangle_x_speed * delta_time
        if self.rectangle_left:
            self.rectangle_x -= self.rectangle_x_speed * delta_time
        if self.rectangle_up:
            self.rectangle_y += self.rectangle_y_speed * delta_time
        if self.rectangle_down:
            self.rectangle_y -= self.rectangle_y_speed * delta_time

    # Setting up input keys
    def on_key_press(self, symbol: int, modifiers: int):
        # inputs for player
        """
        if symbol == arcade.key.D:
            self.go_right = True
        if symbol == arcade.key.A:
            self.go_left = True
        if symbol == arcade.key.W:
            self.player_sprite.strafe(1)
            self.go_up = True
        if symbol == arcade.key.S:
            self.go_down = True"""

        # inputs for player
        self.player.on_key_press(symbol, modifiers)

        # inputs for rectangle
        if symbol == arcade.key.RIGHT:
            self.rectangle_right = True
        if symbol == arcade.key.LEFT:
            self.rectangle_left = True
        if symbol == arcade.key.UP:
            self.rectangle_up = True
        if symbol == arcade.key.DOWN:
            self.rectangle_down = True

    def on_key_release(self, symbol: int, modifiers: int):
        # Inputs for player
        """
        if symbol == arcade.key.D:
            self.go_right = False
        if symbol == arcade.key.A:
            self.go_left = False
        if symbol == arcade.key.W:
            self.go_up = False
        if symbol == arcade.key.S:
            self.go_down = False"""

        # Inputs for player
        self.player.on_key_release(symbol, modifiers)

        # inputs for rectangle
        if symbol == arcade.key.RIGHT:
            self.rectangle_right = False
        if symbol == arcade.key.LEFT:
            self.rectangle_left = False
        if symbol == arcade.key.UP:
            self.rectangle_up = False
        if symbol == arcade.key.DOWN:
            self.rectangle_down = False

    # Setting up mouse follow
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.c_x = x
            self.c_y = y
            self.c_x_speed *= -1
            self.c_y_speed *= -1

        if button == arcade.MOUSE_BUTTON_RIGHT:
            self.rectangle_x = x
            self.rectangle_y = y

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.co_x_speed = x
        self.co_y_speed = y

    def move_cursor(self):
        co_x_dist = self.co_x_speed - self.co_x
        co_y_dist = self.co_y_speed - self.co_y

        # distance = sqrt(co_x_dist * co_x_dist + co_y_dist * co_y_dist)#not optimized
        distance = pow(co_x_dist * co_x_dist + co_y_dist * co_y_dist, 0.5)

        if distance > 1:
            self.co_x += co_x_dist * 0.1
            self.co_y += co_y_dist * 0.1


# Creating my window
MyGameWindow(1280, 720, "Mistery Library")
arcade.run()
