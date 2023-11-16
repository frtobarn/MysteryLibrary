import arcade
import os
from math import sqrt


class MyGameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(0, 0)

        arcade.set_background_color(arcade.color.BLACK)

        # Member variables
        self.tiled_map = None
        self.scene = None

        self.setup()

    def setup(self):
        tiledmap_filepath = (
            os.path.dirname(os.path.abspath(__file__)) + "/Maps/my-map.tmx"
        )

        layer_options = {
            "Terrain": {
                "use_spatial_hash": True,
            },
        }
        self.tiled_map = arcade.load_tilemap(tiledmap_filepath, 0.4, layer_options)

        self.scene = arcade.Scene.from_tilemap(self.tiled_map)
        # --- Other stuff
        # Set the background color
        if self.tiled_map.background_color:
            arcade.set_background_color(self.tiled_map.background_color)

        # Create the 'physics engine'
        """self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, gravity_constant=1, walls=self.scene["Terrain"]
        )"""

    def on_draw(self):
        """Render the screen."""

        # Clear the screen to the background color
        self.clear()

        # Draw our Scene
        self.scene.draw()

        # arcade.start_render()

    def update(self, delta_time):
        """Movement and game logic"""

        # Move the player with the physics engine
        # self.physics_engine.update()
        pass


MyGameWindow(1200, 720, "Tiled maps")
arcade.run()
