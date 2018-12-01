"""
    Ahira Justice, ADEFOKUN
    justiceahira@gmail.com
"""


import os
import sys
import pygame


class Text:
    def __init__(self, DISPLAYSURF):
        self.DISPLAYSURF = DISPLAYSURF

    def makeText(self, text, color, FONT, centerx, top):
        # create the Surface and Rect objects for some text.
        textSurf = FONT.render(text, True, color)
        textRect = textSurf.get_rect()
        textRect.midtop = (centerx, top)
        return (textSurf, textRect)


    def printText(self, msg, FONT, color, centerx, top):
        textSurf, textRect = self.makeText(msg, color, FONT, centerx, top)
        self.DISPLAYSURF.blit(textSurf, textRect)
