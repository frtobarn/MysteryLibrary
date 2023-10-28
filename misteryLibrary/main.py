"""
Mistery library
"""
"""
authors:
Fabian Ricardo Tobar Numesqui
Maria Camila Diaz Guevara
"""

# Importing arcade library
import arcade
from math import sqrt

# from typing import Optional, Tuple
# import pyglet


# Class to setup my custom window
class MyGameWindow(arcade.Window):
    def __init__(
        self,
        width: int = 800,
        height: int = 600,
        title: str | None = "Ghost Library",
        fullscreen: bool = False,
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
        super().__init__(width, height, title, fullscreen)
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

        # Animated sprites
        self.player_list = None
        self.player = None

        # Introducing a sprite
        self.player_sprite = arcade.Sprite(
            "misteryLibrary/sprites/character.png",
            center_x=100,
            center_y=100,
        )
        self.coin_sprite = arcade.Sprite(
            "misteryLibrary/sprites/coin_01.png",
            center_x=200,
            center_y=200,
        )
        self.box_sprite = arcade.Sprite(
            "misteryLibrary/sprites/boxCrate_double.png",
            center_x=300,
            center_y=300,
        )

        # Using spritelist
        self.sprite_list = arcade.SpriteList()
        self.sprite_list.append(self.player_sprite)
        self.sprite_list.append(self.coin_sprite)
        self.sprite_list.append(self.box_sprite)

        # Position vars for Player
        self.player_x = 150
        self.player_y = 50
        self.player_ang = 0

        # Speed vasr for Player
        self.player_x_speed = 100
        self.player_y_speed = 100
        self.player_ang_speed = 0

        # Booleans for player's movement
        self.go_right = False
        self.go_left = False
        self.go_up = False
        self.go_down = False

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
        self.setup()

    #
    def setup(self):
        self.player_list = arcade.SpriteList()
        self.player = arcade.AnimatedWalkingSprite()

        self.player.stand_right_textures = []
        self.player.stand_right_textures.append(
            arcade.load_texture("misteryLibrary/sprites/basicWalk/tile000.png")
        )

        self.player.stand_left_textures = []
        self.player.stand_left_textures.append(
            arcade.load_texture(
                "misteryLibrary/sprites/basicWalk/tile000.png", mirrored=True
            )
        )

        # walk to right sprites
        self.player.walk_right_textures = []
        self.player.walk_right_textures.append(
            arcade.load_texture("misteryLibrary/sprites/basicWalk/tile000.png")
        )
        self.player.walk_right_textures.append(
            arcade.load_texture("misteryLibrary/sprites/basicWalk/tile001.png")
        )
        self.player.walk_right_textures.append(
            arcade.load_texture("misteryLibrary/sprites/basicWalk/tile002.png")
        )
        self.player.walk_right_textures.append(
            arcade.load_texture("misteryLibrary/sprites/basicWalk/tile003.png")
        )
        self.player.walk_right_textures.append(
            arcade.load_texture("misteryLibrary/sprites/basicWalk/tile004.png")
        )
        self.player.walk_right_textures.append(
            arcade.load_texture("misteryLibrary/sprites/basicWalk/tile005.png")
        )
        self.player.walk_right_textures.append(
            arcade.load_texture("misteryLibrary/sprites/basicWalk/tile006.png")
        )
        self.player.walk_right_textures.append(
            arcade.load_texture("misteryLibrary/sprites/basicWalk/tile007.png")
        )

        # walk to left sprites
        self.player.walk_left_textures = []
        self.player.walk_left_textures.append(
            arcade.load_texture(
                "misteryLibrary/sprites/basicWalk/tile000.png", mirrored=True
            )
        )
        self.player.walk_left_textures.append(
            arcade.load_texture(
                "misteryLibrary/sprites/basicWalk/tile001.png", mirrored=True
            )
        )
        self.player.walk_left_textures.append(
            arcade.load_texture(
                "misteryLibrary/sprites/basicWalk/tile002.png", mirrored=True
            )
        )
        self.player.walk_left_textures.append(
            arcade.load_texture(
                "misteryLibrary/sprites/basicWalk/tile003.png", mirrored=True
            )
        )
        self.player.walk_left_textures.append(
            arcade.load_texture(
                "misteryLibrary/sprites/basicWalk/tile004.png", mirrored=True
            )
        )
        self.player.walk_left_textures.append(
            arcade.load_texture(
                "misteryLibrary/sprites/basicWalk/tile005.png", mirrored=True
            )
        )
        self.player.walk_left_textures.append(
            arcade.load_texture(
                "misteryLibrary/sprites/basicWalk/tile006.png", mirrored=True
            )
        )
        self.player.walk_left_textures.append(
            arcade.load_texture(
                "misteryLibrary/sprites/basicWalk/tile007.png", mirrored=True
            )
        )

        self.player.scale = 0.5
        self.player.center_x = 1280 // 2
        self.player.center_y = 720 // 2

        self.player_list.append(self.player)

    # called once a frame to render the window
    def on_draw(self):
        # Gets the setup to render
        arcade.start_render()

        # Drawing animated sprite
        self.player_list.draw()

        # Drawing a sprite
        self.sprite_list.draw()
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

        # Detecting inputs for player
        if self.go_right:
            # self.player_x += self.player_x_speed * delta_time
            self.player_sprite.turn_right(2)
        if self.go_left:
            # self.player_x -= self.player_x_speed * delta_time
            self.player_sprite.turn_left(2)
        if self.go_up:
            # self.player_y += self.player_y_speed * delta_time
            # self.player_sprite.strafe(0.1)
            pass
        if self.go_down:
            # self.player_y -= self.player_y_speed * delta_time
            pass

        # self.player_sprite.set_position(self.player_x, self.player_y)
        # self.player_sprite.update()
        self.sprite_list.update()

        # update animated sprite list
        self.player_list.update()
        self.player_list.update_animation()

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
        if symbol == arcade.key.D:
            self.player.change_x = 5
        if symbol == arcade.key.A:
            self.player.change_x = -5
        if symbol == arcade.key.W:
            self.player.change_y = 5
        if symbol == arcade.key.S:
            self.player.change_y = -5

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
        if symbol == arcade.key.A or symbol == arcade.key.D:
            self.player.change_x = 0
        if symbol == arcade.key.W or symbol == arcade.key.S:
            self.player.change_y = 0

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

    #


# Creating my window
MyGameWindow(1280, 720, "Mistery Library")
arcade.run()
