"""
    Ahira Justice, ADEFOKUN
    justiceahira@gmail.com
"""


import sys
import chess
import chess.pgn

import inout
import ai
import eval
import display.display as display

AI1 = True
AI2 = False

ai1file = inout.readFile('evaluate/black.eval')
ai2file = inout.readFile('evaluate/white.eval')


def displayBoard(board):
    assert type(board) is chess.Board, 'Incorrect object type: %s' % (board.__class__)
    print()
    print(board)


def makeBestMove(bestMove, board):
    board.push(bestMove)

    return bestMove.uci()


def run():
    depth = 3

    board = chess.Board()
    game = chess.pgn.Game()
    game.setup(board)
    node = game

    ai1 = ai.AI(ai1file, 1)
    ai2 = ai.AI(ai2file, 2)

    '''board.turn = False'''

    print("\n-----START-----")
    display.start()

    while not board.is_game_over():
        display.checkForQuit()

        if board.turn is AI1:
            bestMove = ai1.getBestMove(board, depth)
            move = makeBestMove(bestMove, board)
        
        elif board.turn is AI2:
            bestMove = ai2.getBestMove(board, depth)
            move = makeBestMove(bestMove, board)

        node = node.add_variation(bestMove)
        display.update(board.fen())
        display.checkForQuit()

    game.headers["Result"] = board.result()
    exporter = chess.pgn.StringExporter(columns=None, headers=False, comments=False, variations=True)
    gamepgn = game.accept(exporter)

    print("\n---Game-Over---")
    return gamepgn

def main(clargv):
    if len(clargv) < 3:
        sys.exit()

    gamepgn = ''
    count = 0
    while count < int(clargv[1]):
        gamepgn = run()
        print(gamepgn)
        if count == 0:
            inout.writeToFile(gamepgn, 'pgns/' + clargv[2], 'w')
        elif count > 0:
            inout.writeToFile(gamepgn, 'pgns/' + clargv[2], 'a')

        gamepgn = ''
        count += 1


if __name__ == '__main__':
    main(sys.argv)
