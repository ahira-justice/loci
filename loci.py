import sys
import chess

from eval import *

AI = False
PLAYER = True


def display_board(board):
    assert type(board) is chess.Board, 'Incorrect object type: %s' % board.__class__
    print()
    print(board)


def get_legal_moves(board):
    assert type(board) is chess.Board, 'Incorrect object type: %s' % board.__class__

    moves = []
    for move in board.legal_moves:
        moves.append(move)
    
    return moves


def get_absolute_value(piece, piece_color, x, y):
    if piece.piece_type == chess.PAWN:
        return 10 + (pawn_eval_white[y][x] if piece_color is chess.WHITE else pawn_eval_black[y][x])
    elif piece.piece_type == chess.ROOK:
        return 50 + (rook_eval_white[y][x] if piece_color is chess.WHITE else rook_eval_black[y][x])
    elif piece.piece_type == chess.KNIGHT:
        return 50 + knight_eval[y][x]
    elif piece.piece_type == chess.BISHOP:
        return 50 + (bishop_eval_white[y][x] if piece_color is chess.WHITE else bishop_eval_black[y][x])
    elif piece.piece_type == chess.QUEEN:
        return 50 + queen_eval[y][x]
    elif piece.piece_type == chess.KING:
        return 50 + (king_eval_white[y][x] if piece_color is chess.WHITE else king_eval_black[y][x])
    else:
        assert "Unknown piece type: " + piece.piece_type
        sys.exit()


def get_piece_value(piece, x, y):
    if piece is None:
        return 0

    absolute_value = get_absolute_value(piece, piece.color, x, y)
    return absolute_value if piece.color is chess.WHITE else -absolute_value


def evaluate_board(board):
    assert type(board) is chess.Board, 'Incorrect object type: %s' % board.__class__

    total_evaluation = 0

    for i in list(range(8)):
        for j in list(range(8)):
            total_evaluation += get_piece_value(board.piece_at(chess.square(j, i)), i, j)

    return total_evaluation


def minimax(depth, board, alpha, beta, is_maximising_player):
    assert type(board) is chess.Board, 'Incorrect object type: %s' % board.__class__

    if depth == 0:
        return -evaluate_board(board)

    new_game_moves = get_legal_moves(board)

    if is_maximising_player is True:
        best_move = -9999
        for new_game_move in new_game_moves:
            board.push(new_game_move)
            best_move = max(best_move, minimax(depth - 1, board, alpha, beta, not is_maximising_player))
            board.pop()
            alpha = max(alpha, best_move)

            if beta <= alpha:
                return best_move
        
        return best_move
    
    elif is_maximising_player is False:
        best_move = 9999
        for new_game_move in new_game_moves:
            board.push(new_game_move)
            best_move = min(best_move, minimax(depth - 1, board, alpha, beta, not is_maximising_player))
            board.pop()
            beta = min(beta, best_move)

            if beta <= alpha:
                return best_move
        
        return best_move


def minimax_root(depth, board, is_maximising_player):
    assert type(board) is chess.Board, 'Incorrect object type: %s' % board.__class__

    new_game_moves = get_legal_moves(board)
    best_move = -9999
    best_move_found = 0

    for new_game_move in new_game_moves:
        board.push(new_game_move)
        value = minimax(depth - 1, board, -10000, 10000, not is_maximising_player)
        board.pop()

        if value >= best_move:
            best_move = value
            best_move_found = new_game_move

    return best_move_found


def get_best_move(board):
    assert type(board) is chess.Board, 'Incorrect object type: %s' % board.__class__

    if board.is_game_over():
        print("Game over")
        sys.exit()

    depth = 3
    bestMove = minimax_root(depth, board, True)

    return bestMove


def make_best_move(board):
    assert type(board) is chess.Board, 'Incorrect object type: %s' % board.__class__

    best_move = get_best_move(board)
    board.push(best_move)

    return best_move.uci()


def get_user_input():
    return input("\nPlayer turn: ")


def main():
    board = chess.Board()

    print("\n-----START-----")
    display_board(board)

    while not board.is_checkmate():

        if board.turn is PLAYER:
            user_input = get_user_input()
            move = chess.Move.from_uci(user_input)

            if user_input is 'quit':
                break

            if move in get_legal_moves(board):
                board.push(move)
            else:
                print("Invalid Move.")

        elif board.turn is AI:
            move = make_best_move(board)
            print("\nAI turn: " + move)
        
        display_board(board)

    print("\n---Game-Over---")


if __name__ == '__main__':
    main()
