import os
import sys
import random
import chess
import inout
import aieval


ai1 = inout.readFile('evaluate/black.eval')
ai2 = inout.readFile('evaluate/white.eval')

ai1eval = aieval.AIEval(ai1, 1)
ai2eval = aieval.AIEval(ai2, 2)

