import arcade
import os
from game_object import GameObject

PATH = os.path.dirname(os.path.abspath(__file__)) + "/"


class Book(GameObject):
    def __init__(self, name, pos_x, pos_y, author):
        super().__init__(name, pos_x, pos_y)
        self.author = author
        self.clue_sprite = arcade.Sprite(
            PATH + "sprites/books/" + name + ".png",
            center_x=pos_x,
            center_y=pos_y,
        )
