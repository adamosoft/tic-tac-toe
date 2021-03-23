import pygame as pg
import sys
from logic import Tic_tac_toe
from pygame.locals import *


class Game:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.ready_to_reset = False

        #loading the images
        self.x_img = pg.image.load('x.png')
        self.o_img = pg.image.load('o.png')
        #resizing images
        self.x_img = pg.transform.scale(self.x_img, (80,80))    # vylepšiť scale v zavislosti od width, height
        self.o_img = pg.transform.scale(self.o_img, (80,80))
        #initializing pygame window
        self.fps = 30
        self.CLOCK = pg.time.Clock()
        pg.init()
        pg.display.set_caption("Tic Tac Toe")
        self.screen = pg.display.set_mode((self.width, self.height),0,32)
        self.initialize()   # draw game board


    def initialize(self):
        """
        Draw clear game board
        """

        self.ready_to_reset = False
        self.game = Tic_tac_toe()   # create logic object

        line_color = (10,10,10)
        self.screen.fill((255,255,255))

        # Drawing vertical lines
        pg.draw.line(self.screen,line_color,(self.width/3,0),(self.width/3, self.height),7)
        pg.draw.line(self.screen,line_color,(self.width/3*2,0),(self.width/3*2, self.height),7)
        # Drawing horizontal lines
        pg.draw.line(self.screen,line_color,(0,self.height/3),(self.width, self.height/3),7)
        pg.draw.line(self.screen,line_color,(0,self.height/3*2),(self.width, self.height/3*2),7)

        pg.display.update()


    def draw_XO(self,row, column, player):

        # evaluating where to draw image
        if row == 1:
            posx = 30
        if row == 2:
            posx = int(self.width/3) + 30
        if row == 3:
            posx = int(self.width/3*2) + 30

        if column == 1:
            posy = 30
        if column == 2:
            posy = int(self.height/3) + 30
        if column == 3:
            posy = int(self.height/3*2) + 30

        # Displayed image depends on which player's move is
        if player == 1:
            self.screen.blit(self.x_img,(posy,posx))
        else:
            self.screen.blit(self.o_img,(posy,posx))

        pg.display.update() #refresh


    def click(self):

        # get mouse pos
        x,y = pg.mouse.get_pos()

        # evaluating where has player clicked
        if(x<self.width/3):
            col = 1
        elif (x<self.width/3*2):
            col = 2
        elif(x<self.width):
            col = 3
        else:
            col = None
            
        # row
        if(y<self.height/3):
            row = 1
        elif (y<self.height/3*2):
            row = 2
        elif(y<self.height):
            row = 3
        else:
            row = None

        valid_move = True
        # adding move to logic engine
        if self.game.desk[row - 1][col - 1] == None:    # If this place has not been already taken
            self.game.desk[row - 1][col - 1] = self.game.players[self.game.player]
        else:
            valid_move = False

        # if noone has won
        if self.game.evaluate_win() != None:
            self.game.winner = self.game.player
        # if it is not draw
        if self.game.evaluate_draw() == True:
            self.game.draw = True

        # draw move
        if valid_move:
            self.draw_XO(row, col, self.game.player)

            # change player
            if self.game.player == 1:
              self.game.player = 2
            else:
              self.game.player = 1


    def ending(self,winner):
        """
        Ending screen
        """

        white = (255, 255, 255)
        black = (0, 0, 0)
        self.screen.fill(black)


        if self.game.winner:
            message = f"Player {winner} has won the game!"
        else:
            message = "Draw!"

        # Display text
        font = pg.font.Font(None, 32)
        text = font.render(message, True, white, black)
        textRect = text.get_rect(center = self.screen.get_rect().center)
        self.screen.blit(text, textRect)

        pg.display.update()
        self.ready_to_reset = True

    def run(self):
        """
        Pygame loop
        """

        while True:
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type is MOUSEBUTTONDOWN:

                    self.click()
                    if self.ready_to_reset:
                        self.initialize()
                    if self.game.winner or self.game.draw:
                        self.ending(self.game.winner)
                        

            pg.display.update()
            self.CLOCK.tick(self.fps)


game = Game(400,400)
game.run()
