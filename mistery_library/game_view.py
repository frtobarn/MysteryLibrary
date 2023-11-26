import arcade
from game_over_view import GameOverView


from ghost import Ghost
from fading_view import FadingView
from player import Player
from config import Config
from map import Map

# from pause_view import PauseView


config = Config()

# Physics
MOVEMENT_SPEED = 8
JUMP_SPEED = 28
GRAVITY = 0.0


# inherit from FAdingView to use transition
class GameView(FadingView):
    def __init__(self):
        super().__init__()
        # Create variables here# creating a level or map
        self.level_1 = Map("level_1")

        # Creating a player and some ghosts
        start_pos = (config.screen_half_width, config.screen_half_height)
        self.player = Player("player", start_pos[0], start_pos[1], 100)

        # Creating some ghosts
        self.ghost_1 = Ghost("ghost_1", 100, 150, 0.001, "", "")
        self.ghost_2 = Ghost("ghost_2", 200, 250, 0.001, "", "")
        self.ghost_3 = Ghost("ghost_3", 300, 350, 0.001, "", "")
        self.ghost_4 = Ghost("ghost_4", 400, 450, 0.001, "", "")
        self.ghost_5 = Ghost("ghost_5", 500, 550, 0.001, "", "")

        """# Player sprite lists
        self.player_sprite_list = self.player.character_sprite_list.sprite_list
        # Ghosts sprite lists
        self.ghost_1_sprite_list = self.ghost_1.character_sprite_list.sprite_list"""

        # Physics
        self.physics_engine = None

        # introducing score
        self.score = 200

        # Running setup fuction
        self.setup()

    def setup(self):
        # print(type(self.player.character_sprite_list.sprite_list))

        # Generate a list of all sprites that collided with the player.
        """hit_list = arcade.check_for_collision_with_list(
            self.player_sprite_list, self.ghost_1_sprite_list
        )"""

        # Loop through each colliding sprite, remove it, and add to the
        # score.
        """for ghost in hit_list:
            ghost.kill()
            self.score += 1
            self.window.total_score += 1"""

        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player.character_sprite,
            self.level_1.scene.get_sprite_list("walls"),
            gravity_constant=GRAVITY,
        )

    # On_update function(called every frame)
    def on_update(self, delta_time: float):
        # Updating physics engine
        self.physics_engine.update()
        # updating player's animated sprite list
        self.player.update()

        # moving camera
        self.move_camera()

        # Executing ghost's logic
        self.ghost_1.update(delta_time)
        self.ghost_2.update(delta_time)
        self.ghost_3.update(delta_time)
        self.ghost_4.update(delta_time)
        self.ghost_5.update(delta_time)

        # Fading in
        self.update_fade(next_view=GameOverView)

    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)

    # Called once a frame to render the window
    def on_draw(self):
        # Clear the screen to load the background color
        self.clear()

        # Gets the setup to render
        arcade.start_render()

        # Drawing tiled map
        self.level_1.draw()

        # Drawing player's  and ghost's animated sprite
        self.player.draw()
        self.ghost_1.draw()
        self.ghost_2.draw()
        self.ghost_3.draw()
        self.ghost_4.draw()
        self.ghost_5.draw()

        # Drawing optinos on screen
        # self.draw_info()

        # drawing score
        output = f"Score: {self.score}"
        arcade.draw_text(
            output,
            arcade.get_viewport()[0] + 10,
            arcade.get_viewport()[2] + 30,
            arcade.color.WHITE,
            14,
        )
        output_total = f"Total Score: {self.window.total_score}"
        arcade.draw_text(
            output_total,
            arcade.get_viewport()[0] + 10,
            arcade.get_viewport()[2] + 10,
            arcade.color.WHITE,
            14,
        )

        # fading in-out
        self.draw_fading()

    # Setting up input keys
    def on_key_press(self, symbol: int, modifiers: int):
        # inputs for player
        self.player.on_key_press(symbol, modifiers)

        if symbol == arcade.key.SPACE:
            game_over_view = GameOverView()
            game_over_view.score = self.score
            self.fade_out = 0

        if symbol == arcade.key.ESCAPE:
            # pass self, the current view, to preserve this view's state
            pause = PauseView(self)
            self.window.show_view(pause)

    def on_key_release(self, symbol: int, modifiers: int):
        # Inputs for player
        self.player.on_key_release(symbol, modifiers)

    # Setting up mouse follow

    # Getting inputs from mouse
    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.player.on_mouse_motion(x, y)

    # Inputs for light mouse's buttons
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        self.player.light.on_mouse_press(x, y, button, modifiers)

    # Claculating camera movement
    def clamp(self, value, mini, maxi):
        return max(min(value, maxi), mini)

    # moving camera
    def move_camera(self):
        # moving camera
        self.player.character_sprite.center_x = self.clamp(
            self.player.character_sprite.center_x, 0, self.level_1.width
        )

        self.player.character_sprite.center_y = self.clamp(
            self.player.character_sprite.center_y, 0, self.level_1.height
        )

        if (
            self.player.character_sprite.center_x > config.screen_half_width
            and self.player.character_sprite.center_x
            < self.level_1.width - self.level_1.tile_width - config.screen_half_width
            or self.player.character_sprite.center_y > config.screen_half_height
            and self.player.character_sprite.center_y
            < self.level_1.height - self.level_1.tile_height - config.screen_half_height
        ):
            change_view = True
        else:
            change_view = False

        if change_view:
            arcade.set_viewport(
                self.player.character_sprite.center_x - config.screen_half_width,
                self.player.character_sprite.center_x + config.screen_half_width,
                self.player.character_sprite.center_y - config.screen_half_height,
                self.player.character_sprite.center_y + config.screen_half_height,
            )

    def move_camera1(self):
        # moving camera
        self.player.character_sprite.center_x = self.clamp(
            self.player.character_sprite.center_x, 0, self.level_1.width
        )

        if (
            self.player.character_sprite.center_x > config.screen_half_width
            and self.player.character_sprite.center_x
            < self.level_1.width - self.level_1.tile_width - config.screen_half_width
        ):
            change_view = True
        else:
            change_view = False

        if change_view:
            arcade.set_viewport(
                self.player.character_sprite.center_x - config.screen_half_width,
                self.player.character_sprite.center_x + config.screen_half_width,
                0,
                config.screen_height,
            )

    # drawing interface
    def draw_info(self):
        # return
        # Drawing a frame
        # self.player.character_sprite.sprite_lists[0].sprite_list[0] # sprite class
        arcade.draw_lines(
            [
                (0, 0),
                (config.screen_width, 0),
                (config.screen_width, 0),
                (config.screen_width, config.screen_height),
                (config.screen_width, config.screen_height),
                (0, config.screen_height),
                (0, config.screen_height),
                (0, 0),
            ],
            arcade.color.ALABAMA_CRIMSON,
            10,
        )
        # Drawing score text
        arcade.draw_text(
            f"Score: {self.score}",
            arcade.get_viewport()[0] + 10,
            arcade.get_viewport()[2] + config.screen_height - 30,
            arcade.color.GOLD,
            font_size=20,
        )


class PauseView(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view
        self.background_color = arcade.color.BLUE_GRAY

    def on_show_view(self):
        arcade.set_background_color(self.background_color)

    def on_draw(self):
        self.clear()

        # Draw player, for effect, on pause screen.
        # The previous View (GameView) was passed in
        # and saved in self.game_view.

        player_sprite = self.game_view.player.character_sprite.sprite_lists[
            0
        ].sprite_list[0]
        player_sprite.draw()

        # draw an orange filter over him first
        arcade.draw_lrtb_rectangle_filled(
            left=player_sprite.left - config.player_sprite_width // 4,
            right=player_sprite.right - config.player_sprite_width // 4,
            top=player_sprite.top - config.player_sprite_height // 4,
            bottom=player_sprite.bottom - config.player_sprite_height // 4,
            color=self.background_color + (200,),
        )

        arcade.draw_text(
            "PAUSED",
            arcade.get_viewport()[0] + config.screen_half_width,
            arcade.get_viewport()[2] + config.screen_half_height + 50,
            arcade.color.WHITE,
            font_size=50,
            anchor_x="center",
        )

        # Show tip to return or reset
        arcade.draw_text(
            "Press Esc. to return",
            arcade.get_viewport()[0] + config.screen_half_width,
            arcade.get_viewport()[2] + config.screen_half_height,
            arcade.color.BLACK,
            font_size=20,
            anchor_x="center",
        )
        arcade.draw_text(
            "Press Enter to reset",
            arcade.get_viewport()[0] + config.screen_half_width,
            arcade.get_viewport()[2] + config.screen_half_height - 30,
            arcade.color.BLACK,
            font_size=20,
            anchor_x="center",
        )

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:  # resume game
            self.window.show_view(self.game_view)
        elif key == arcade.key.ENTER:  # reset game
            game = GameView()
            self.window.show_view(game)
