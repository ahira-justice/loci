import sys
import chess


def reverse_list(_list):
    return _list[::-1]


class AIEval:
    def __init__(self, eval_file, state):
        if state == 1:
            self.pawn_eval_white = eval_file[0]
            self.pawn_eval_black = reverse_list(self.pawn_eval_white)

            self.bishop_eval_white = eval_file[1]
            self.bishop_eval_black = reverse_list(self.bishop_eval_white)

            self.rook_eval_white = eval_file[2]
            self.rook_eval_black = reverse_list(self.rook_eval_white)

            self.knight_eval = eval_file[3]

            self.queen_eval = eval_file[4]

            self.king_eval_white = eval_file[5]
            self.king_eval_black = reverse_list(self.king_eval_white)

        elif state == 2:
            self.pawn_eval_black = eval_file[0]
            self.pawn_eval_white = reverse_list(self.pawn_eval_black)

            self.bishop_eval_black = eval_file[1]
            self.bishop_eval_white = reverse_list(self.bishop_eval_black)

            self.rook_eval_black = eval_file[2]
            self.rook_eval_white = reverse_list(self.rook_eval_black)

            self.knight_eval = eval_file[3]

            self.queen_eval = eval_file[4]

            self.king_eval_black = eval_file[5]
            self.king_eval_white = reverse_list(self.king_eval_black)

    def get_absolute_value(self, piece, piece_color, x, y):
        if piece.piece_type == chess.PAWN:
            return 10 + (self.pawn_eval_white[y][x] if piece_color is chess.WHITE else self.pawn_eval_black[y][x])
        elif piece.piece_type == chess.ROOK:
            return 50 + (self.rook_eval_white[y][x] if piece_color is chess.WHITE else self.rook_eval_black[y][x])
        elif piece.piece_type == chess.KNIGHT:
            return 50 + self.knight_eval[y][x]
        elif piece.piece_type == chess.BISHOP:
            return 50 + (self.bishop_eval_white[y][x] if piece_color is chess.WHITE else self.bishop_eval_black[y][x])
        elif piece.piece_type == chess.QUEEN:
            return 50 + self.queen_eval[y][x]
        elif piece.piece_type == chess.KING:
            return 50 + (self.king_eval_white[y][x] if piece_color is chess.WHITE else self.king_eval_black[y][x])
        else:
            assert "Unknown piece type: " + piece.piece_type
            sys.exit()

    def get_piece_value(self, piece, x, y):
        if piece is None:
            return 0

        absolute_value = self.get_absolute_value(piece, piece.color, x, y)
        return absolute_value if piece.color is chess.WHITE else -absolute_value

    def evaluate_board(self, board):
        assert type(board) is chess.Board, 'Incorrect object type: %s' % board.__class__

        total_evaluation = 0

        for i in list(range(8)):
            for j in list(range(8)):
                total_evaluation += self.get_piece_value(board.piece_at(chess.square(j, i)), i, j)

        return total_evaluation
