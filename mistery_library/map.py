import arcade
import os


class Map:
    def __init__(self, name):
        # Member variables
        self.name = name
        self.tiled_map = None
        self.scene = None

        self.setup()

    def setup(self):
        tiledmap_filepath = (
            os.path.dirname(os.path.abspath(__file__)) + "/maps/my-map.tmx"
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

    def draw(self):
        # Drawing our Scene
        self.scene.draw()

    def update(self):
        pass
