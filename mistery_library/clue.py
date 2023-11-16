import arcade
import os
from game_object import GameObject

PATH = os.path.dirname(os.path.abspath(__file__)) + "/"


class Clue(GameObject):
    def __init__(self, name, pos_x, pos_y, clue_text):
        super().__init__(name, pos_x, pos_y)
        self.clue_text = clue_text
        self.clue_sprite = arcade.Sprite(
            PATH + "sprites/clues/" + name + ".png",
            center_x=pos_x,
            center_y=pos_y,
        )
