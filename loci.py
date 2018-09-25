"""
    Ahira Justice, ADEFOKUN
    justiceahira@gmail.com
"""


import os
import sys
import random
import chess


AI = False
PLAYER = True


def reverseList(_list):
    return _list[::-1]


pawnEvalWhite = [
    [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
    [5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0],
    [1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0],
    [0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5],
    [0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0],
    [0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5],
    [0.5,  1.0, 1.0,  -2.0, -2.0,  1.0,  1.0,  0.5],
    [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]
]

pawnEvalBlack = reverseList(pawnEvalWhite)

bishopEvalWhite = [
    [ -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
    [ -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
    [ -1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0],
    [ -1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0],
    [ -1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0],
    [ -1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0],
    [ -1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0],
    [ -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]
]

bishopEvalBlack = reverseList(bishopEvalWhite)

rookEvalWhite = [
    [  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
    [  0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [  0.0,   0.0, 0.0,  0.5,  0.5,  0.0,  0.0,  0.0]
]

rookEvalBlack = reverseList(rookEvalWhite)

knightEval = [
    [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
    [-4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0],
    [-3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0],
    [-3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0],
    [-3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0],
    [-3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0],
    [-4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0],
    [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]
]

evalQueen = [
    [ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
    [ -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
    [ -1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
    [ -0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
    [  0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
    [ -1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
    [ -1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0],
    [ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]
]

kingEvalWhite = [
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
    [ -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
    [  2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0 ],
    [  2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0 ]
]

kingEvalBlack = reverseList(kingEvalWhite)

def displayBoard(board):
    assert type(board) is chess.Board, 'Incorrect object type: %s' % (board.__class__)
    print()
    print(board)

def getLegalMoves(board):
    assert type(board) is chess.Board, 'Incorrect object type: %s' % (board.__class__)

    moves = []
    for move in board.legal_moves:
        moves.append(move)
    
    return moves

def getAbsoluteValue(piece, piece_color, x, y):
    if (piece.piece_type == chess.PAWN):
        return 10 + (pawnEvalWhite[y][x] if piece_color is chess.WHITE else pawnEvalBlack[y][x])
    elif (piece.piece_type == chess.ROOK):
        return 50 + (rookEvalWhite[y][x] if piece_color is chess.WHITE else rookEvalBlack[y][x])
    elif (piece.piece_type == chess.KNIGHT):
        return 50 + knightEval[y][x]
    elif (piece.piece_type == chess.BISHOP):
        return 50 + (bishopEvalWhite[y][x] if piece_color is chess.WHITE else bishopEvalBlack[y][x])
    elif (piece.piece_type == chess.QUEEN):
        return 50 + evalQueen[y][x]
    elif (piece.piece_type == chess.KING):
        return 50 + (kingEvalWhite[y][x] if piece_color is chess.WHITE else kingEvalBlack[y][x])
    else:
        assert "Unknown piece type: " + piece.piece_type
        sys.exit()


def getPieceValue(piece, x, y):
    if (piece is None):
        return 0

    absoluteValue = getAbsoluteValue(piece, piece.color, x, y)
    return absoluteValue if piece.color is chess.WHITE else -absoluteValue


def evaluateBoard(board):
    assert type(board) is chess.Board, 'Incorrect object type: %s' % (board.__class__)

    totalEvaluation = 0

    for i in list(range(8)):
        for j in list(range(8)):
            totalEvaluation += getPieceValue(board.piece_at(chess.square(j, i)), i, j)

    return totalEvaluation


def minimax(depth, board, alpha, beta, isMaximisingPlayer):
    assert type(board) is chess.Board, 'Incorrect object type: %s' % (board.__class__)

    if depth == 0:
        return -evaluateBoard(board)

    newGameMoves = getLegalMoves(board)

    if isMaximisingPlayer is True:
        bestMove = -9999
        for newGameMove in newGameMoves:
            board.push(newGameMove)
            bestMove = max(bestMove, minimax(depth - 1, board, alpha, beta, not isMaximisingPlayer))
            board.pop()
            alpha = max(alpha, bestMove)

            if beta <= alpha:
                return bestMove
        
        return bestMove
    
    elif isMaximisingPlayer is False:
        bestMove = 9999
        for newGameMove in newGameMoves:
            board.push(newGameMove)
            bestMove = min(bestMove, minimax(depth - 1, board, alpha, beta, not isMaximisingPlayer))
            board.pop()
            beta = min(beta, bestMove)

            if beta <= alpha:
                return bestMove
        
        return bestMove


def minimaxRoot(depth, board, isMaximisingPlayer):
    assert type(board) is chess.Board, 'Incorrect object type: %s' % (board.__class__)

    newGameMoves = getLegalMoves(board)
    bestMove = -9999
    bestMoveFound = 0

    for newGameMove in newGameMoves:
        board.push(newGameMove)
        value = minimax(depth-1, board, -10000, 10000, not isMaximisingPlayer)
        board.pop()

        if value >= bestMove:
            bestMove = value
            bestMoveFound = newGameMove

    return bestMoveFound


def getBestMove(board):
    assert type(board) is chess.Board, 'Incorrect object type: %s' % (board.__class__)

    if board.is_game_over():
        print("Game over")
        sys.exit()

    depth = 3
    bestMove = minimaxRoot(depth, board, True)

    return bestMove


def makeBestMove(board):
    assert type(board) is chess.Board, 'Incorrect object type: %s' % (board.__class__)

    bestMove = getBestMove(board)
    board.push(bestMove)


def getUserInput():
    return input("\nPlayer turn: ")


def main():
    board = chess.Board()

    print("\n-----START-----")
    displayBoard(board)

    while not board.is_checkmate():

        if board.turn is PLAYER:
            user_input = getUserInput()
            move = chess.Move.from_uci(user_input)

            if user_input is 'quit':
                break

            if move in getLegalMoves(board):
                board.push(move)
            else:
                print("Invalid Move.")

        elif board.turn is AI:
            makeBestMove(board)
            print("\nAI turn: ")
        
        displayBoard(board)


if __name__ == '__main__':
    main()
