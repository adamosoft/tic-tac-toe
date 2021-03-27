from draw import Game
from process_file import load_config


config = load_config("config.txt")
width = int(config["width"])
height = int(config["height"])


game = Game(width, height)
game.run()
