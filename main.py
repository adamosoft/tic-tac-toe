from multiplayer import Multiplayer
from singleplayer import Singleplayer
from process_file import load_config
from pygame.locals import *
from intro import intro, start
import pygame as pg
import sys


config = load_config("config.txt")
width = int(config["width"])
height = int(config["height"])


if intro(width, height) == "Singleplayer":
    game = Singleplayer(width, height)
    game.run()
else:
    game = Multiplayer(width, height)
    game.run()

