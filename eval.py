"""
    Ahira Justice, ADEFOKUN
    justiceahira@gmail.com
"""


import sys
import chess


class AIEval:
    def __init__(self, evalfile, state):
        if state == 1:
            self.pawnEvalWhite = evalfile[0]
            self.pawnEvalBlack = self.reverseList(self.pawnEvalWhite)

            self.bishopEvalWhite = evalfile[1]
            self.bishopEvalBlack = self.reverseList(self.bishopEvalWhite)

            self.rookEvalWhite = evalfile[2]
            self.rookEvalBlack = self.reverseList(self.rookEvalWhite)

            self.knightEval = evalfile[3]

            self.evalQueen = evalfile[4]

            self.kingEvalWhite = evalfile[5]
            self.kingEvalBlack = self.reverseList(self.kingEvalWhite)

        elif state == 2:
            self.pawnEvalBlack = evalfile[0]
            self.pawnEvalWhite = self.reverseList(self.pawnEvalBlack)

            self.bishopEvalBlack = evalfile[1]
            self.bishopEvalWhite = self.reverseList(self.bishopEvalBlack)

            self.rookEvalBlack = evalfile[2]
            self.rookEvalWhite = self.reverseList(self.rookEvalBlack)

            self.knightEval = evalfile[3]

            self.evalQueen = evalfile[4]

            self.kingEvalBlack = evalfile[5]
            self.kingEvalWhite = self.reverseList(self.kingEvalBlack)


    def reverseList(self, _list):
        return _list[::-1]


    def getAbsoluteValue(self, piece, piece_color, x, y):
        if (piece.piece_type == chess.PAWN):
            return 10 + (self.pawnEvalWhite[y][x] if piece_color is chess.WHITE else self.pawnEvalBlack[y][x])
        elif (piece.piece_type == chess.ROOK):
            return 50 + (self.rookEvalWhite[y][x] if piece_color is chess.WHITE else self.rookEvalBlack[y][x])
        elif (piece.piece_type == chess.KNIGHT):
            return 50 + self.knightEval[y][x]
        elif (piece.piece_type == chess.BISHOP):
            return 50 + (self.bishopEvalWhite[y][x] if piece_color is chess.WHITE else self.bishopEvalBlack[y][x])
        elif (piece.piece_type == chess.QUEEN):
            return 50 + self.evalQueen[y][x]
        elif (piece.piece_type == chess.KING):
            return 50 + (self.kingEvalWhite[y][x] if piece_color is chess.WHITE else self.kingEvalBlack[y][x])
        else:
            assert "Unknown piece type: " + piece.piece_type
            sys.exit()


    def getPieceValue(self, piece, x, y):
        if (piece is None):
            return 0

        absoluteValue = self.getAbsoluteValue(piece, piece.color, x, y)
        return absoluteValue if piece.color is chess.WHITE else -absoluteValue


    def evaluateBoard(self, board):
        assert type(board) is chess.Board, 'Incorrect object type: %s' % (board.__class__)

        totalEvaluation = 0

        for i in list(range(8)):
            for j in list(range(8)):
                totalEvaluation += self.getPieceValue(board.piece_at(chess.square(j, i)), i, j)

        return totalEvaluation
