"""
    Ahira Justice, ADEFOKUN
    justiceahira@gmail.com
"""


import os
import sys
import pygame


class Board:
    a8, a7, a6, a5, a4, a3, a2, a1 = (100, 100), (100, 150), (100, 200), (100, 250), (100, 300), (100, 350), (100, 400), (100, 450)
    b8, b7, b6, b5, b4, b3, b2, b1 = (150, 100), (150, 150), (150, 200), (150, 250), (150, 300), (150, 350), (150, 400), (150, 450)
    c8, c7, c6, c5, c4, c3, c2, c1 = (200, 100), (200, 150), (200, 200), (200, 250), (200, 300), (200, 350), (200, 400), (200, 450)
    d8, d7, d6, d5, d4, d3, d2, d1 = (250, 100), (250, 150), (250, 200), (250, 250), (250, 300), (250, 350), (250, 400), (250, 450)
    e8, e7, e6, e5, e4, e3, e2, e1 = (300, 100), (300, 150), (300, 200), (300, 250), (300, 300), (300, 350), (300, 400), (300, 450)
    f8, f7, f6, f5, f4, f3, f2, f1 = (350, 100), (350, 150), (350, 200), (350, 250), (350, 300), (350, 350), (350, 400), (350, 450)
    g8, g7, g6, g5, g4, g3, g2, g1 = (400, 100), (400, 150), (400, 200), (400, 250), (400, 300), (400, 350), (400, 400), (400, 450)
    h8, h7, h6, h5, h4, h3, h2, h1 = (450, 100), (450, 150), (450, 200), (450, 250), (450, 300), (450, 350), (450, 400), (450, 450)
    
    posb = [
        [a8, b8, c8, d8, e8, f8, g8, h8],
        [a7, b7, c7, d7, e7, f7, g7, h7]
        ]
    
    posw = [
        [a2, b2, c2, d2, e2, f2, g2, h2],
        [a1, b1, c1, d1, e1, f1, g1, h1]
        ]
    
    boardRect = (
        (a8, b8, c8, d8, e8, f8, g8, h8),
        (a7, b7, c7, d7, e7, f7, g7, h7),
        (a6, b6, c6, d6, e6, f6, g6, h6),
        (a5, b5, c5, d5, e5, f5, g5, h5),
        (a4, b4, c4, d4, e4, f4, g4, h4),
        (a3, b3, c3, d3, e3, f3, g3, h3),
        (a2, b2, c2, d2, e2, f2, g2, h2),
        (a1, b1, c1, d1, e1, f1, g1, h1)
    )

    btile = pygame.image.load('images/btile.png')
    wtile = pygame.image.load('images/wtile.png')

    def __init__(self, colors, BGCOLOR, DISPLAYSURF):
        self.colors = colors
        self.BGCOLOR = BGCOLOR
        self.DISPLAYSURF = DISPLAYSURF


    def displayBoard(self):
        self.DISPLAYSURF.fill(self.BGCOLOR)
        pygame.draw.rect(self.DISPLAYSURF, self.colors['Black'], (95, 95, 410, 410), 10)

        for i in range(1, len(Board.boardRect)+1):
            for j in range(1, len(Board.boardRect[i-1])+1):
                if self.isOdd(i):
                    if self.isOdd(j):
                        self.DISPLAYSURF.blit(Board.wtile, Board.boardRect[i-1][j-1])
                    elif self.isEven(j):
                        self.DISPLAYSURF.blit(Board.btile, Board.boardRect[i-1][j-1])
                elif self.isEven(i):
                    if self.isOdd(j):
                        self.DISPLAYSURF.blit(Board.btile, Board.boardRect[i-1][j-1])
                    elif self.isEven(j):
                        self.DISPLAYSURF.blit(Board.wtile, Board.boardRect[i-1][j-1])


    def isOdd(self, number):
        if number % 2 == 1:
            return True
        return


    def isEven(self, number):
        if number % 2 == 0:
            return True
        return