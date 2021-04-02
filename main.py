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

def main():

    if intro(width, height) == "Singleplayer":
        game = Singleplayer(width, height)
        #ESC pressed
        if game.run() is None:
            main()
    else:
        game = Multiplayer(width, height)
        #ESC pressed
        if game.run() is None:
            main()

if __name__ == "__main__":
    main()

