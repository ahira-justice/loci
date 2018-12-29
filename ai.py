"""
    Ahira Justice, ADEFOKUN
    justiceahira@gmail.com
"""


import sys
import chess
import eval


class AI:
    def __init__(self, evalfile, state):
        self.state = state
        self.eval = eval.AIEval(evalfile, state)


    def getLegalMoves(self, board):
        assert type(board) is chess.Board, 'Incorrect object type: %s' % (board.__class__)

        moves = []
        for move in board.legal_moves:
            moves.append(move)
        
        return moves


    def minimax(self, depth, board, alpha, beta, isMaximisingPlayer):
        assert type(board) is chess.Board, 'Incorrect object type: %s' % (board.__class__)

        if depth == 0:
            return -self.eval.evaluateBoard(board)

        newGameMoves = self.getLegalMoves(board)

        if isMaximisingPlayer is True:
            bestMove = -9999
            for newGameMove in newGameMoves:
                board.push(newGameMove)
                bestMove = max(bestMove, self.minimax(depth - 1, board, alpha, beta, not isMaximisingPlayer))
                board.pop()
                alpha = max(alpha, bestMove)

                if beta <= alpha:
                    return bestMove
            
            return bestMove
        
        elif isMaximisingPlayer is False:
            bestMove = 9999
            for newGameMove in newGameMoves:
                board.push(newGameMove)
                bestMove = min(bestMove, self.minimax(depth - 1, board, alpha, beta, not isMaximisingPlayer))
                board.pop()
                beta = min(beta, bestMove)

                if beta <= alpha:
                    return bestMove
            
            return bestMove


    def minimaxRoot(self, depth, board, isMaximisingPlayer):
        assert type(board) is chess.Board, 'Incorrect object type: %s' % (board.__class__)

        newGameMoves = self.getLegalMoves(board)
        bestMove = -9999
        bestMoveFound = 0

        for newGameMove in newGameMoves:
            board.push(newGameMove)
            value = self.minimax(depth-1, board, -10000, 10000, not isMaximisingPlayer)
            board.pop()

            if value >= bestMove:
                bestMove = value
                bestMoveFound = newGameMove

        return bestMoveFound


    def getBestMove(self, board, depth):
        assert type(board) is chess.Board, 'Incorrect object type: %s' % (board.__class__)

        if self.state == 1:
            bestMove = self.minimaxRoot(depth, board, True)
        elif self.state == 2:
            bestMove = self.minimaxRoot(depth, board, False)

        return bestMove
