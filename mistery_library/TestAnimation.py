import arcade
import os
from math import sqrt

SPRITE_WIDTH = 80
SPRITE_HEIGHT = 100


class MyGameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(0, 00)

        arcade.set_background_color(arcade.color.WHITE)

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
            os.path.dirname(os.path.abspath(__file__)) + "/sprites/ghosts/ghost_1.png"
        )
        # print(sprite_filepath)

        """for i in range(9):
            texture = arcade.load_texture(
                sprite_filepath, x=i * 100, y=0, width=100, height=442
            )
            anim = arcade.AnimationKeyframe(i, 30, texture)
            self.player.frames.append(anim)"""

        duration = 240
        for i in range(3):
            texture = arcade.load_texture(
                sprite_filepath,
                x=SPRITE_WIDTH * i,
                y=0,
                width=SPRITE_WIDTH,
                height=SPRITE_HEIGHT,
            )
            anim = arcade.AnimationKeyframe(i + 1, duration, texture)
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
