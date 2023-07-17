import logging

import chess
import chess.pgn
import click

from chessboard import display

import ai
import fileio

logging.basicConfig(format='%(asctime)s | %(name)s | %(levelname)s | %(message)s')
logger = logging.getLogger(__name__)

LOG_LEVELS = ['CRITICAL', 'FATAL', 'ERROR', 'WARNING', 'WARN', 'INFO', 'DEBUG', 'NOTSET']
LOG_LEVELS_CHOICE = click.Choice(LOG_LEVELS, case_sensitive=False)

AI1 = chess.WHITE
AI2 = chess.BLACK

ai1file = fileio.read('evaluate/white.eval.txt')
ai2file = fileio.read('evaluate/black.eval.txt')


def make_best_move(best_move, board):
    board.push(best_move)


def run():
    depth = 3

    board = chess.Board()
    game = chess.pgn.Game()
    game.setup(board)
    node = game

    ai1 = ai.AI(ai1file, 1)
    ai2 = ai.AI(ai2file, 2)

    display_board = display.start()

    while not board.is_game_over():
        display.check_for_quit()

        if board.turn is AI1:
            best_move = ai1.get_best_move(board, depth)
            make_best_move(best_move, board)

        elif board.turn is AI2:
            best_move = ai2.get_best_move(board, depth)
            make_best_move(best_move, board)

        node = node.add_variation(best_move)
        display.update(board.fen(), display_board)
        display.check_for_quit()

    game.headers["Result"] = board.result()
    exporter = chess.pgn.StringExporter(columns=None, headers=False, comments=False, variations=True)
    game_pgn = game.accept(exporter)

    return game_pgn


@click.command()
@click.option('-c', '--count', default=1, help='Number of games')
@click.option('-l', '--log-level', default='INFO', help='Output log level', type=LOG_LEVELS_CHOICE)
@click.argument('output_file')
def main(count, log_level, output_file):
    logger.level = logging.getLevelName(log_level)

    game = 1

    logger.info("start")
    while game <= count:
        logger.debug("game %s", game)

        game_pgn = run()
        if game == 1:
            fileio.write(f"{game_pgn}\n", output_file, 'w')
        else:
            fileio.write(f"{game_pgn}\n", output_file, 'a')

        logger.debug(game_pgn)

        game += 1

    logger.info("end")


if __name__ == '__main__':
    main()
