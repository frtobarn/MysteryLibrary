import os
import arcade
from character import Character
from light import Light

# Getting absolute path because im into a virtual environment
PATH = os.path.dirname(os.path.abspath(__file__)) + "/"


class Player(Character):
    def __init__(self, name, pos_x, pos_y, speed, sprite_path):
        super().__init__(name, pos_x, pos_y, speed, sprite_path)

        # Position vars for Player
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.player_ang = 0

        # Speed vasr for Player
        self.speed = speed
        self.player_y_speed = 100

        # Booleans for player's movement
        self.go_right = False
        self.go_left = False
        self.go_up = False
        self.go_down = False

        # Light from cellphone
        self.light = Light("Cellphone light", pos_x, pos_y, 100, 100)
        self.player_ang_speed = 0

        # Animated sprites
        self.player_list = None
        self.player = None

        # Running animated sprite setup function
        self.setup()

    # Animated sprite setup function
    def setup(self):
        # print(PATH)

        # Here i want to saved mi spritesheet animation
        self.player_list = arcade.SpriteList()
        self.player = arcade.AnimatedWalkingSprite()

        self.player.stand_right_textures = []
        self.player.stand_right_textures.append(
            arcade.load_texture(PATH + "sprites/basicWalk/tile000.png")
        )

        self.player.stand_left_textures = []
        self.player.stand_left_textures.append(
            arcade.load_texture(PATH + "sprites/basicWalk/tile000.png", mirrored=True)
        )

        # walk to right sprites
        self.player.walk_right_textures = []
        self.player.walk_right_textures.append(
            arcade.load_texture(PATH + "sprites/basicWalk/tile000.png")
        )
        self.player.walk_right_textures.append(
            arcade.load_texture(PATH + "sprites/basicWalk/tile001.png")
        )
        self.player.walk_right_textures.append(
            arcade.load_texture(PATH + "sprites/basicWalk/tile002.png")
        )
        self.player.walk_right_textures.append(
            arcade.load_texture(PATH + "sprites/basicWalk/tile003.png")
        )
        self.player.walk_right_textures.append(
            arcade.load_texture(PATH + "sprites/basicWalk/tile004.png")
        )
        self.player.walk_right_textures.append(
            arcade.load_texture(PATH + "sprites/basicWalk/tile005.png")
        )
        self.player.walk_right_textures.append(
            arcade.load_texture(PATH + "sprites/basicWalk/tile006.png")
        )
        self.player.walk_right_textures.append(
            arcade.load_texture(PATH + "sprites/basicWalk/tile007.png")
        )

        # walk to left sprites
        self.player.walk_left_textures = []
        self.player.walk_left_textures.append(
            arcade.load_texture(PATH + "sprites/basicWalk/tile000.png", mirrored=True)
        )
        self.player.walk_left_textures.append(
            arcade.load_texture(PATH + "sprites/basicWalk/tile001.png", mirrored=True)
        )
        self.player.walk_left_textures.append(
            arcade.load_texture(PATH + "sprites/basicWalk/tile002.png", mirrored=True)
        )
        self.player.walk_left_textures.append(
            arcade.load_texture(PATH + "sprites/basicWalk/tile003.png", mirrored=True)
        )
        self.player.walk_left_textures.append(
            arcade.load_texture(PATH + "sprites/basicWalk/tile004.png", mirrored=True)
        )
        self.player.walk_left_textures.append(
            arcade.load_texture(PATH + "sprites/basicWalk/tile005.png", mirrored=True)
        )
        self.player.walk_left_textures.append(
            arcade.load_texture(PATH + "sprites/basicWalk/tile006.png", mirrored=True)
        )
        self.player.walk_left_textures.append(
            arcade.load_texture(PATH + "sprites/basicWalk/tile007.png", mirrored=True)
        )

        self.player.scale = 0.5
        self.player.center_x = 1280 // 2
        self.player.center_y = 720 // 2

        self.player_list.append(self.player)

    def draw(self):
        # Drawing player's animated sprite
        self.player_list.draw()

    def update(self):
        # update plater's animated sprite list
        self.player_list.update()
        self.player_list.update_animation()

    def move(self):
        # Detecting inputs for player
        if self.go_right:
            # self.player_x += self.player_x_speed * delta_time
            self.player_sprite.turn_right(2)
        if self.go_left:
            # self.player_x -= self.player_x_speed * delta_time
            self.player_sprite.turn_left(2)
        if self.go_up:
            # self.player_y += self.player_y_speed * delta_time
            # self.player_sprite.strafe(0.1)
            pass
        if self.go_down:
            # self.player_y -= self.player_y_speed * delta_time
            pass

    def on_key_press(self, symbol: int, modifiers: int):
        # inputs for player
        if symbol == arcade.key.D:
            self.player.change_x = 5
        if symbol == arcade.key.A:
            self.player.change_x = -5
        if symbol == arcade.key.W:
            self.player.change_y = 5
        if symbol == arcade.key.S:
            self.player.change_y = -5

    def on_key_release(self, symbol: int, modifiers: int):
        # Inputs for player
        if symbol == arcade.key.A or symbol == arcade.key.D:
            self.player.change_x = 0
        if symbol == arcade.key.W or symbol == arcade.key.S:
            self.player.change_y = 0

    def turn_on_light(self):
        self.light.turn_on()

    def turn_off_light(self):
        self.light.turn_off()

    def die(self):
        pass
