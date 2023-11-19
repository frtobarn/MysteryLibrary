import arcade
from game_object import GameObject
from config import Config

# singleton
config = Config()


class Book(GameObject):
    def __init__(self, name, pos_x, pos_y, author):
        super().__init__(name, pos_x, pos_y)
        self.author = author
        self.clue_sprite = arcade.Sprite(
            config.path + "sprites/books/" + name + ".png",
            center_x=pos_x,
            center_y=pos_y,
        )
