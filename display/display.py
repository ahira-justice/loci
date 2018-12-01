"""
    Ahira Justice, ADEFOKUN
    justiceahira@gmail.com
"""


import os
import sys
import time
import pygame
from pygame.locals import *

import board
import event


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


def main():
    global DISPLAYSURF,BASICFONT
    pygame.init()

    # Setting up the GUI window.
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('LOCI')
    BASICFONT = pygame.font.SysFont('calibri', BASICFONTSIZE)

    DISPLAYSURF.fill(BGCOLOR)
    gameboard = board.Board(colors, BGCOLOR, DISPLAYSURF)

    while True:
        event.checkForQuit()
        gameboard.displayBoard()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

    event.terminate()


if __name__ == '__main__':
    main()
