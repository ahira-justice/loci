"""
    Ahira Justice, ADEFOKUN
    justiceahira@gmail.com
"""


import os
import sys
import pygame


class Board:
    def __init__(self, colors, BGCOLOR, DISPLAYSURF):
        self.colors = colors
        self.BGCOLOR = BGCOLOR
        self.DISPLAYSURF = DISPLAYSURF

        #self.boardrect = 

    def displayBoard(self):
        self.DISPLAYSURF.fill(self.BGCOLOR)
        pygame.draw.rect(self.DISPLAYSURF, self.colors['Black'], (95, 95, 410, 410), 10)
