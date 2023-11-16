import arcade
import os
from character import Character


class Ghost(Character):
    def __init__(
        self, name, pos_x, pos_y, speed, sprite_path, movement_style, target_book
    ):
        super().__init__(name, pos_x, pos_y, speed, sprite_path)

        self.movement_style = movement_style
        self.target_book = target_book

        self.ghost_list = None
        self.ghost = None

        self.setup()

    def setup(self):
        # First set the playerlist and player vars
        self.ghost_list = arcade.SpriteList()
        self.ghost = arcade.AnimatedTimeBasedSprite()

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
        self.ghost.frames.append(anim)

        texture = arcade.load_texture(
            sprite_filepath, x=160, y=0, width=160, height=292
        )
        anim = arcade.AnimationKeyframe(2, duration, texture)
        self.ghost.frames.append(anim)

        texture = arcade.load_texture(
            sprite_filepath, x=320, y=0, width=160, height=292
        )
        anim = arcade.AnimationKeyframe(3, duration, texture)
        self.ghost.frames.append(anim)

        texture = arcade.load_texture(
            sprite_filepath, x=480, y=0, width=160, height=292
        )
        anim = arcade.AnimationKeyframe(4, duration, texture)
        self.ghost.frames.append(anim)

        texture = arcade.load_texture(
            sprite_filepath, x=0, y=292, width=160, height=292
        )
        anim = arcade.AnimationKeyframe(5, duration, texture)
        self.ghost.frames.append(anim)

        texture = arcade.load_texture(
            sprite_filepath, x=160, y=292, width=160, height=292
        )
        anim = arcade.AnimationKeyframe(6, duration, texture)
        self.ghost.frames.append(anim)

        texture = arcade.load_texture(
            sprite_filepath, x=320, y=292, width=160, height=292
        )
        anim = arcade.AnimationKeyframe(7, duration, texture)
        self.ghost.frames.append(anim)

        texture = arcade.load_texture(
            sprite_filepath, x=480, y=292, width=160, height=292
        )
        anim = arcade.AnimationKeyframe(8, duration, texture)
        self.ghost.frames.append(anim)

        self.ghost.center_x = self.pos_x
        self.ghost.center_y = self.pos_y

        self.ghost_list.append(self.ghost)

    def draw(self):
        self.ghost_list.draw()

    def update(self):
        self.ghost_list.update_animation()

    def disapear():
        pass

    def attack():
        pass

    def flee():
        pass

    def chase_player():
        pass
