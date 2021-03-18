import pygame as pg
import sys
from tictactoe import Tic_tac_toe
from pygame.locals import *

# initialize global variables
width = 400
height = 400

#initializing pygame window
pg.init()
fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height),0,32)
pg.display.set_caption("Tic Tac Toe")
line_color = (10,10,10)
screen.fill((255,255,255))

# Drawing vertical lines
pg.draw.line(screen,line_color,(width/3,0),(width/3, height),7)
pg.draw.line(screen,line_color,(width/3*2,0),(width/3*2, height),7)
# Drawing horizontal lines
pg.draw.line(screen,line_color,(0,height/3),(width, height/3),7)
pg.draw.line(screen,line_color,(0,height/3*2),(width, height/3*2),7)

#loading the images
x_img = pg.image.load('x.png')
o_img = pg.image.load('o.png')

#resizing images
x_img = pg.transform.scale(x_img, (80,80))
o_img = pg.transform.scale(o_img, (80,80))


game = Tic_tac_toe()


def draw_XO(row, column, player):

    if row == 1:
        posx = 30
    if row == 2:
        posx = int(width/3) + 30
    if row == 3:
        posx = int(width/3*2) + 30

    if column == 1:
        posy = 30
    if column == 2:
        posy = int(height/3) + 30
    if column == 3:
        posy = int(height/3*2) + 30

    if player == 1:
        screen.blit(x_img,(posy,posx))
    else:
        screen.blit(o_img,(posy,posx))

    pg.display.update()


def click():
    # mouse pos
    x,y = pg.mouse.get_pos()
    # column
    if(x<width/3):
        col = 1
    elif (x<width/3*2):
        col = 2
    elif(x<width):
        col = 3
    else:
        col = None
        
    # row
    if(y<height/3):
        row = 1
    elif (y<height/3*2):
        row = 2
    elif(y<height):
        row = 3
    else:
        row = None

    game.desk[row - 1][col - 1] = game.players[game.player]
    if game.evaluate_win() != None:
        game.winner = game.player
    if game.evaluate_draw() == True:
        game.draw = True

    draw_XO(row, col, game.player)
    if game.player == 1:
      game.player = 2
    else:
      game.player = 1

def ending(winner):
    white = (255, 255, 255)
    black = (0, 0, 0)
    screen.fill(black)
    if not game.draw:
        message = f"Player {winner} has won the game!"
    else:
        message = "Draw!"
    font = pg.font.Font(None, 32)
    text = font.render(message, True, white, black)
    textRect = text.get_rect(center = screen.get_rect().center)
    screen.blit(text, textRect)
    pg.display.update()

# run the game loop forever
while(True):
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type is MOUSEBUTTONDOWN:
            # the user clicked; place an X or O
            click()
            if game.winner or game.draw:
                ending(game.winner)

            
    pg.display.update()
    CLOCK.tick(fps)
