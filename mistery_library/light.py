import arcade
from game_object import GameObject
from config import Config

config = Config()


class Light(GameObject):
    def __init__(self, name, pos_x, pos_y, range, batery_level):
        super().__init__(name, pos_x, pos_y)

        # Custom cursor
        self.pos_x = 150
        self.pos_y = 50
        self.range = range
        self.batery_level = batery_level
        self.x_speed = 0
        self.y_speed = 0

        #
        self.object_sprite = arcade.Sprite(config.path + "sprites/utils/lightRange.png")
        self.setup()

    def setup(self):
        self.object_sprite.center_x = self.pos_x
        self.object_sprite.center_y = self.pos_y
        self.object_sprite.scale = 2
        self.object_sprite.alpha = 200

    # Drawing light
    def draw(self):
        arcade.draw_circle_outline(
            self.pos_x, self.pos_y, 30, arcade.color.APRICOT, 3, 0, 10
        )
        self.object_sprite.draw()

    # Updating light
    def update(self):
        self.move()
        self.object_sprite.center_x = self.pos_x
        self.object_sprite.center_y = self.pos_y
        # self.object_sprite.update()

    # Getting input from mouse
    def on_mouse_motion(self, x, y):
        self.x_speed = x
        self.y_speed = y

    # moving light
    def move(self):
        light_x_dist = self.x_speed - self.pos_x
        light_y_dist = self.y_speed - self.pos_y

        # distance = sqrt(co_x_dist * co_x_dist + co_y_dist * co_y_dist)#not optimized
        distance = pow(light_x_dist * light_x_dist + light_y_dist * light_y_dist, 0.5)

        if distance > 1:
            self.pos_x += light_x_dist * 0.1
            self.pos_y += light_y_dist * 0.1

    # Inputs for light object
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.pos_x = x
            self.pos_y = y
            # self.x_speed *= -1
            # self.y_speed *= -1

        if button == arcade.MOUSE_BUTTON_RIGHT:
            # self.rectangle_x = x
            # self.rectangle_y = y
            pass

    def turn_on():
        pass

    def turn_off():
        pass
