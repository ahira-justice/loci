"""
    Ahira Justice, ADEFOKUN
    justiceahira@gmail.com
"""


import os
import sys
import pygame

BLACK = 'BLACK'
WHITE = 'WHITE'

BISHOP = 'BISHOP'
KING = 'KING'
KNGHT = 'KNIGHT'
PAWN = 'PAWN'
QUEEN = 'QUEEN'
ROOK = 'ROOK'


class Piece:
    bBishop = pygame.image.load('images/bB.png')
    bKing = pygame.image.load('images/bK.png')
    bKnight = pygame.image.load('images/bN.png')
    bPawn = pygame.image.load('images/bP.png')
    bQueen = pygame.image.load('images/bQ.png')
    bRook = pygame.image.load('images/bR.png')

    wBishop = pygame.image.load('images/wB.png')
    wKing = pygame.image.load('images/wK.png')
    wKnight = pygame.image.load('images/wN.png')
    wPawn = pygame.image.load('images/wP.png')
    wQueen = pygame.image.load('images/wQ.png')
    wRook = pygame.image.load('images/wR.png')

    def __init__(self, color, piece, DISPLAYSURF):
        self.position = None
        self.sprite = None
        self.DISPLAYSURF = DISPLAYSURF

        self.color = color
        self.piece = piece

        self.setSprite()

    def setPosition(self, position):
        self.position = position
    

    def setSprite(self):
        if self.color == BLACK:
            if self.piece == BISHOP:
                self.sprite = Piece.bBishop
            elif self.piece == KING:
                self.sprite = Piece.bKing
            elif self.piece == KNGHT:
                self.sprite = Piece.bKnight
            elif self.piece == PAWN:
                self.sprite = Piece.bPawn
            elif self.piece == QUEEN:
                self.sprite = Piece.bQueen
            elif self.piece == ROOK:
                self.sprite = Piece.bRook
        elif self.color == WHITE:
            if self.piece == BISHOP:
                self.sprite = Piece.wBishop
            elif self.piece == KING:
                self.sprite = Piece.wKing
            elif self.piece == KNGHT:
                self.sprite = Piece.wKnight
            elif self.piece == PAWN:
                self.sprite = Piece.wPawn
            elif self.piece == QUEEN:
                self.sprite = Piece.wQueen
            elif self.piece == ROOK:
                self.sprite = Piece.wRook


    def displayPiece(self):
        self.DISPLAYSURF.blit(self.sprite, self.position)
