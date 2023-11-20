# Sprite size in px
SPRITE_WIDTH = 0
SPRITE_HEIGHT = 0


class Character:
    def __init__(self, name, pos_x, pos_y, speed):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = speed
        self.character_sprite = None
        self.character_sprite_list = None

    def draw(self):
        pass

    def move():
        pass

    def detect_outbounds():
        pass
