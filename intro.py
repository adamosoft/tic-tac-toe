from pygame.locals import *
import pygame as pg
import sys


def start(y:int, height: int) -> None:
    """
    Starting game
    y - y-coord of mouse-click
    """

    if y > height // 2:
        return "Multiplayer"
    else:
        return "Singleplayer"


def intro(width:int, height:int) -> None:
    """
    Intro-screen
    """

    fps = 30
    CLOCK = pg.time.Clock()
    pg.init()
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption("Select gamemode")

    white = (255,255,255)
    black = (0, 0, 0)

    pg.draw.line(screen,white,(0, height // 2),(width, height // 2),7)
    # Singleplayer
    font = pg.font.Font(None, 32)
    text = font.render("Singleplayer", True, white, black)
    textRect = text.get_rect(center = (width // 2, height // 4))
    screen.blit(text, textRect)

    # Multiplayer
    font = pg.font.Font(None, 32)
    text = font.render("Multiplayer", True, white, black)
    textRect = text.get_rect(center = (width // 2, height - height // 4))
    screen.blit(text, textRect)

    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

            elif event.type is MOUSEBUTTONDOWN:
                x,y = pg.mouse.get_pos()
                return start(y, height)

            pg.display.update()
            CLOCK.tick(fps)
