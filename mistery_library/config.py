import os

# Getting absolute path because im into a linux virtual environment
PATH = os.path.dirname(os.path.abspath(__file__)) + "/"
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 660


class Config(object):
    __instance = None

    def __new__(cls):
        if Config.__instance is None:
            print("Loading config...")
            Config.__instance = object.__new__(cls)

        return Config.__instance

    def __init__(self):
        self.path = PATH
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT
        self.screen_half_width = SCREEN_WIDTH // 2
        self.screen_half_height = SCREEN_HEIGHT // 2
