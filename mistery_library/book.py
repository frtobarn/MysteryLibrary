from game_object import GameObject


class Book(GameObject):
    def __init__(self, name, pos_x, pos_y):
        super().__init__(name, pos_x, pos_y)
