import arcade
import os
from math import sqrt


class MyGameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(400, 200)

        arcade.set_background_color(arcade.color.BLACK)

        # Member variables
        self.player_list = None
        self.player = None

        self.setup()

    def setup(self):
        # First set the playerlist and player vars
        self.player_list = arcade.SpriteList()
        self.player = arcade.AnimatedTimeBasedSprite()

        # changed from AnimatedTimeSprite
        # self.player.textures = []

        # Getting abslute path for my resources
        sprite_filepath = (
            os.path.dirname(os.path.abspath(__file__)) + "/sprites/walk-basic.png"
        )
        # print(sprite_filepath)

        """for i in range(9):
            texture = arcade.load_texture(
                sprite_filepath, x=i * 100, y=0, width=100, height=442
            )
            anim = arcade.AnimationKeyframe(i, 30, texture)
            self.player.frames.append(anim)"""

        duration = 90

        texture = arcade.load_texture(sprite_filepath, x=0, y=0, width=160, height=292)
        anim = arcade.AnimationKeyframe(1, duration, texture)
        self.player.frames.append(anim)

        texture = arcade.load_texture(
            sprite_filepath, x=160, y=0, width=160, height=292
        )
        anim = arcade.AnimationKeyframe(2, duration, texture)
        self.player.frames.append(anim)

        texture = arcade.load_texture(
            sprite_filepath, x=320, y=0, width=160, height=292
        )
        anim = arcade.AnimationKeyframe(3, duration, texture)
        self.player.frames.append(anim)

        texture = arcade.load_texture(
            sprite_filepath, x=480, y=0, width=160, height=292
        )
        anim = arcade.AnimationKeyframe(4, duration, texture)
        self.player.frames.append(anim)

        texture = arcade.load_texture(
            sprite_filepath, x=0, y=292, width=160, height=292
        )
        anim = arcade.AnimationKeyframe(5, duration, texture)
        self.player.frames.append(anim)

        texture = arcade.load_texture(
            sprite_filepath, x=160, y=292, width=160, height=292
        )
        anim = arcade.AnimationKeyframe(6, duration, texture)
        self.player.frames.append(anim)

        texture = arcade.load_texture(
            sprite_filepath, x=320, y=292, width=160, height=292
        )
        anim = arcade.AnimationKeyframe(7, duration, texture)
        self.player.frames.append(anim)

        texture = arcade.load_texture(
            sprite_filepath, x=480, y=292, width=160, height=292
        )
        anim = arcade.AnimationKeyframe(8, duration, texture)
        self.player.frames.append(anim)

        self.player.center_x = 1280 // 2
        self.player.center_y = 720 // 2

        self.player_list.append(self.player)

    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()

    def update(self, delta_time):
        self.player_list.update_animation()


MyGameWindow(1200, 720, "Animated Spritesheet")
arcade.run()
