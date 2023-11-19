import arcade
from character import Character
from config import Config

# Getting config
# singleton
config = Config()

#
SPRITE_WIDTH = 160
SPRITE_HEIGHT = 292


class Ghost(Character):
    def __init__(
        self,
        name,
        pos_x,
        pos_y,
        speed,
        movement_style,
        target_book,
    ):
        super().__init__(name, pos_x, pos_y, speed)

        self.movement_style = movement_style
        self.target_book = target_book

        # Position var for circle
        self.ang = 0

        # Speed vars for character
        self.ang_speed = 0
        self.direction_x = 1
        self.direction_y = 1

        self.setup()

    def setup(self):
        # Setting up character sprite
        self.character_sprite_list = arcade.SpriteList()
        self.character_sprite = arcade.AnimatedTimeBasedSprite()

        # Getting abslute path for my resources
        sprite_filepath = config.path + "sprites/walk-basic.png"

        """for i in range(9):
            texture = arcade.load_texture(
                sprite_filepath, x=i * 100, y=0, width=100, height=442
            )
            anim = arcade.AnimationKeyframe(i, 30, texture)
            self.player.frames.append(anim)"""

        duration = 90

        texture = arcade.load_texture(
            sprite_filepath, x=0, y=0, width=SPRITE_WIDTH, height=SPRITE_HEIGHT
        )
        anim = arcade.AnimationKeyframe(1, duration, texture)
        self.character_sprite.frames.append(anim)

        texture = arcade.load_texture(
            sprite_filepath,
            x=160,
            y=0,
            width=SPRITE_WIDTH,
            height=SPRITE_HEIGHT,
        )
        anim = arcade.AnimationKeyframe(2, duration, texture)
        self.character_sprite.frames.append(anim)

        texture = arcade.load_texture(
            sprite_filepath,
            x=320,
            y=0,
            width=SPRITE_WIDTH,
            height=SPRITE_HEIGHT,
        )
        anim = arcade.AnimationKeyframe(3, duration, texture)
        self.character_sprite.frames.append(anim)

        texture = arcade.load_texture(
            sprite_filepath,
            x=480,
            y=0,
            width=SPRITE_WIDTH,
            height=SPRITE_HEIGHT,
        )
        anim = arcade.AnimationKeyframe(4, duration, texture)
        self.character_sprite.frames.append(anim)

        texture = arcade.load_texture(
            sprite_filepath,
            x=0,
            y=292,
            width=SPRITE_WIDTH,
            height=SPRITE_HEIGHT,
        )
        anim = arcade.AnimationKeyframe(5, duration, texture)
        self.character_sprite.frames.append(anim)

        texture = arcade.load_texture(
            sprite_filepath,
            x=160,
            y=292,
            width=SPRITE_WIDTH,
            height=SPRITE_HEIGHT,
        )
        anim = arcade.AnimationKeyframe(6, duration, texture)
        self.character_sprite.frames.append(anim)

        texture = arcade.load_texture(
            sprite_filepath,
            x=320,
            y=292,
            width=SPRITE_WIDTH,
            height=SPRITE_HEIGHT,
        )
        anim = arcade.AnimationKeyframe(7, duration, texture)
        self.character_sprite.frames.append(anim)

        texture = arcade.load_texture(
            sprite_filepath,
            x=480,
            y=292,
            width=SPRITE_WIDTH,
            height=SPRITE_HEIGHT,
        )
        anim = arcade.AnimationKeyframe(8, duration, texture)
        self.character_sprite.frames.append(anim)

        self.character_sprite.center_x = self.pos_x
        self.character_sprite.center_y = self.pos_y

        self.character_sprite_list.append(self.character_sprite)

    def draw(self):
        self.character_sprite_list.draw()

    def update(self, delta_time):
        # Moving chracter
        self.move(delta_time)
        # Updating animation sprites
        self.character_sprite_list.update_animation()

    def move(self, delta_time):
        # Trying to move
        self.character_sprite_list.move(self.direction_x, self.direction_y)

        # Updating character position
        pos = self.character_sprite_list.center
        self.pos_x = int(pos[0])
        self.pos_y = int(pos[1])

        # Detecting outbounds
        if (
            self.pos_x + SPRITE_WIDTH // 2 > config.screen_width
            or self.pos_x - SPRITE_WIDTH // 2 < 0
        ):
            self.direction_x *= -1
        if (
            self.pos_y + SPRITE_HEIGHT // 2 > config.screen_height
            or self.pos_y - SPRITE_HEIGHT // 2 < 0
        ):
            self.direction_y *= -1

    def disapear():
        pass

    def attack():
        pass

    def flee():
        pass

    def chase_player():
        pass
