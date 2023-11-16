from game_object import GameObject


class Light(GameObject):
    def __init__(self, name, pos_x, pos_y, range, batery_level):
        super().__init__(name, pos_x, pos_y)
        self.range = range
        self.batery_level = batery_level

    def turn_on():
        pass

    def turn_off():
        pass
