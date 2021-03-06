"""
    Ahira Justice, ADEFOKUN
    justiceahira@gmail.com
"""


import os
import sys
import time
import pygame
from pygame.locals import *

import display.board as board


os.environ['SDL_VIDEO_CENTERED'] = '1' # Centre display window.

FPS = 30
FPSCLOCK = pygame.time.Clock()

colors = {
    'Ash':  ( 50,  50,  50),
    'White':(255, 255, 255),
    'Black':(  0,   0,   0),
}

BGCOLOR = colors['Ash']

WINDOWWIDTH, WINDOWHEIGHT = 600, 600
BASICFONTSIZE = 30


def terminate():
    pygame.quit()
    sys.exit()


def checkForQuit():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        terminate() #terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate() # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event) # put the other KEYUP event objects back


def start():
    global DISPLAYSURF,BASICFONT, gameboard
    pygame.init()

    # Setting up the GUI window.
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('LOCI')
    BASICFONT = pygame.font.SysFont('calibri', BASICFONTSIZE)

    checkForQuit()

    DISPLAYSURF.fill(BGCOLOR)
    gameboard = board.Board(colors, BGCOLOR, DISPLAYSURF)
    gameboard.displayBoard()
    gameboard.drawPieces()
    
    pygame.display.update()
    FPSCLOCK.tick(FPS)

def update(fen):
    checkForQuit()
    gameboard.displayBoard()
    gameboard.updatePieces(fen)
    pygame.display.update()
    FPSCLOCK.tick(FPS)
