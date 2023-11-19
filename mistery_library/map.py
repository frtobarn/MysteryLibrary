import arcade

# importing classes
from clue import Clue

# getting config
from config import Config

# singleton
config = Config()


class Map:
    def __init__(self, name):
        # Member variables
        self.name = name
        self.tiled_map = None
        self.scene = None

        # Creating clues
        self.clue_1 = Clue("clue_1", 900, 600, "")
        self.clue_2 = Clue("clue_2", 300, 300, "")

        # Using a spritelist to store clues
        self.clue_list = arcade.SpriteList()
        self.clue_list.append(self.clue_1.clue_sprite)
        self.clue_list.append(self.clue_2.clue_sprite)

        # setup tiled_map function
        self.setup()

    # setup tiled_map function
    def setup(self):
        tiledmap_filepath = config.path + "maps/my-map.tmx"

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

        # Drawing clues spritelist
        self.clue_list.draw()

    def update(self):
        # Updating clues spritelist
        self.clue_list.update()
