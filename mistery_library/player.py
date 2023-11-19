import arcade
from character import Character
from light import Light

# Getting config
from config import Config

# singleton
config = Config()

SPRITE_WIDTH = 160
SPRITE_HEIGHT = 292


class Player(Character):
    def __init__(self, name, pos_x, pos_y, speed):
        super().__init__(name, pos_x, pos_y, speed)

        # Position vars for Player
        self.player_ang = 0

        # Booleans for player's movement
        self.go_right = False
        self.go_left = False
        self.go_up = False
        self.go_down = False

        # Light from cellphone
        # Creating light
        self.light = Light(
            "Cellphone light",
            config.screen_width // 2,
            config.screen_height // 2,
            10,
            100,
        )

        # Running animated sprite setup function
        self.setup()

    # Animated sprite setup function
    def setup(self):
        # Here i want to saved mi spritesheet animation
        self.character_sprite_list = arcade.SpriteList()
        self.character_sprite = arcade.AnimatedWalkingSprite()

        self.character_sprite.stand_right_textures = []
        self.character_sprite.stand_right_textures.append(
            arcade.load_texture(config.path + "sprites/basicWalk/tile000.png")
        )

        self.character_sprite.stand_left_textures = []
        self.character_sprite.stand_left_textures.append(
            arcade.load_texture(
                config.path + "sprites/basicWalk/tile000.png", mirrored=True
            )
        )

        # walk to right sprites
        self.character_sprite.walk_right_textures = []
        self.character_sprite.walk_right_textures.append(
            arcade.load_texture(config.path + "sprites/basicWalk/tile000.png")
        )
        self.character_sprite.walk_right_textures.append(
            arcade.load_texture(config.path + "sprites/basicWalk/tile001.png")
        )
        self.character_sprite.walk_right_textures.append(
            arcade.load_texture(config.path + "sprites/basicWalk/tile002.png")
        )
        self.character_sprite.walk_right_textures.append(
            arcade.load_texture(config.path + "sprites/basicWalk/tile003.png")
        )
        self.character_sprite.walk_right_textures.append(
            arcade.load_texture(config.path + "sprites/basicWalk/tile004.png")
        )
        self.character_sprite.walk_right_textures.append(
            arcade.load_texture(config.path + "sprites/basicWalk/tile005.png")
        )
        self.character_sprite.walk_right_textures.append(
            arcade.load_texture(config.path + "sprites/basicWalk/tile006.png")
        )
        self.character_sprite.walk_right_textures.append(
            arcade.load_texture(config.path + "sprites/basicWalk/tile007.png")
        )

        # walk to left sprites
        self.character_sprite.walk_left_textures = []
        self.character_sprite.walk_left_textures.append(
            arcade.load_texture(
                config.path + "sprites/basicWalk/tile000.png", mirrored=True
            )
        )
        self.character_sprite.walk_left_textures.append(
            arcade.load_texture(
                config.path + "sprites/basicWalk/tile001.png", mirrored=True
            )
        )
        self.character_sprite.walk_left_textures.append(
            arcade.load_texture(
                config.path + "sprites/basicWalk/tile002.png", mirrored=True
            )
        )
        self.character_sprite.walk_left_textures.append(
            arcade.load_texture(
                config.path + "sprites/basicWalk/tile003.png", mirrored=True
            )
        )
        self.character_sprite.walk_left_textures.append(
            arcade.load_texture(
                config.path + "sprites/basicWalk/tile004.png", mirrored=True
            )
        )
        self.character_sprite.walk_left_textures.append(
            arcade.load_texture(
                config.path + "sprites/basicWalk/tile005.png", mirrored=True
            )
        )
        self.character_sprite.walk_left_textures.append(
            arcade.load_texture(
                config.path + "sprites/basicWalk/tile006.png", mirrored=True
            )
        )
        self.character_sprite.walk_left_textures.append(
            arcade.load_texture(
                config.path + "sprites/basicWalk/tile007.png", mirrored=True
            )
        )

        self.character_sprite.scale = 0.5
        self.character_sprite.center_x = 1280 // 2
        self.character_sprite.center_y = 720 // 2

        self.character_sprite.set_hit_box(
            [
                (0, 0),
                (SPRITE_WIDTH, 0),
                (SPRITE_WIDTH, 0),
                (SPRITE_WIDTH, SPRITE_HEIGHT),
                (SPRITE_WIDTH, SPRITE_HEIGHT),
                (0, SPRITE_HEIGHT),
                (0, SPRITE_HEIGHT),
                (0, 0),
            ]
        )

        self.character_sprite_list.append(self.character_sprite)

    def draw(self):
        # Drawing player's animated sprite
        self.character_sprite_list.draw()

        # Drawing player's light
        self.light.draw()

    def update(self):
        # update plater's animated sprite list
        self.character_sprite_list.update()
        self.character_sprite_list.update_animation()

        # Moving light using mouse's movements
        self.light.update()

        # detecting screen limits
        # self.detect_outbounds()

    def on_key_press(self, symbol: int, modifiers: int):
        # inputs for player
        if symbol == arcade.key.D:
            self.character_sprite.change_x = 5
        if symbol == arcade.key.A:
            self.character_sprite.change_x = -5
        if symbol == arcade.key.W:
            self.character_sprite.change_y = 5
        if symbol == arcade.key.S:
            self.character_sprite.change_y = -5

    def on_key_release(self, symbol: int, modifiers: int):
        # Inputs for player
        if symbol == arcade.key.A or symbol == arcade.key.D:
            self.character_sprite.change_x = 0
        if symbol == arcade.key.W or symbol == arcade.key.S:
            self.character_sprite.change_y = 0

    def detect_outbounds(self):
        pos = self.character_sprite_list.center
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        if self.pos_x > config.screen_width:
            self.character_sprite.set_position(self.pos_x - 1, self.pos_y)

    # Getting inputs from mouse
    def on_mouse_motion(self, x, y):
        self.light.on_mouse_motion(x, y)

    def turn_on_light(self):
        self.light.turn_on()

    def turn_off_light(self):
        self.light.turn_off()

    def die(self):
        pass
