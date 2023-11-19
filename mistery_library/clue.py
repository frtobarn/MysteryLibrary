import arcade
from game_object import GameObject
from config import Config

# singleton
config = Config()


class Clue(GameObject):
    def __init__(self, name, pos_x, pos_y, clue_text):
        super().__init__(name, pos_x, pos_y)
        self.clue_text = clue_text
        self.clue_sprite = arcade.Sprite(
            config.path + "sprites/clues/" + name + ".png",
            center_x=pos_x,
            center_y=pos_y,
        )
