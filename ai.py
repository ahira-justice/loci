import chess
from eval import AIEval


class AI:
    def __init__(self, eval_file, state):
        self.state = state
        self.eval = AIEval(eval_file, state)

    def minimax(self, depth, board, alpha, beta, is_maximising_player):
        assert type(board) is chess.Board, 'Incorrect object type: %s' % board.__class__

        if depth == 0:
            return -self.eval.evaluate_board(board)

        new_game_moves = board.legal_moves

        if is_maximising_player is True:
            best_move = -9999
            for new_game_move in new_game_moves:
                board.push(new_game_move)
                best_move = max(best_move, self.minimax(depth - 1, board, alpha, beta, not is_maximising_player))
                board.pop()
                alpha = max(alpha, best_move)

                if beta <= alpha:
                    return best_move

            return best_move

        elif is_maximising_player is False:
            best_move = 9999
            for new_game_move in new_game_moves:
                board.push(new_game_move)
                best_move = min(best_move, self.minimax(depth - 1, board, alpha, beta, not is_maximising_player))
                board.pop()
                beta = min(beta, best_move)

                if beta <= alpha:
                    return best_move

            return best_move

    def minimax_root(self, depth, board, is_maximising_player):
        assert type(board) is chess.Board, 'Incorrect object type: %s' % board.__class__

        new_game_moves = board.legal_moves
        best_move = -9999
        best_move_found = 0

        for new_game_move in new_game_moves:
            board.push(new_game_move)
            value = self.minimax(depth - 1, board, -10000, 10000, not is_maximising_player)
            board.pop()

            if value >= best_move:
                best_move = value
                best_move_found = new_game_move

        return best_move_found

    def get_best_move(self, board, depth):
        assert type(board) is chess.Board, 'Incorrect object type: %s' % board.__class__

        if self.state == 1:
            best_move = self.minimax_root(depth, board, True)
        elif self.state == 2:
            best_move = self.minimax_root(depth, board, False)

        return best_move
