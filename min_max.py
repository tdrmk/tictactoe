import math
from tictaetoe import TicTacToe


def min_max(tictactoe: TicTacToe, maximizing_player=True, player='X'):
    if tictactoe.game_over:
        return tictactoe.score(player), None, 1

    if maximizing_player:
        # evaluated positions just contains the number of explored positions.
        max_eval, max_pos, evaluated_positions = -math.inf, None, 0

        for pos in tictactoe.pending:
            new_tictactoe = tictactoe.copy()
            new_tictactoe.make_move(pos)
            cur_eval, _, c = min_max(new_tictactoe, False, player)
            if max_eval < cur_eval:
                max_eval, max_pos = cur_eval, pos

            evaluated_positions += c

        return max_eval, max_pos, evaluated_positions

    else:
        min_eval, min_pos, evaluated_positions = +math.inf, None, 0
        for pos in tictactoe.pending:
            new_tictactoe = tictactoe.copy()
            new_tictactoe.make_move(pos)
            cur_eval, _, c = min_max(new_tictactoe, True, player)
            if min_eval > cur_eval:
                min_eval, min_pos = cur_eval, pos

            evaluated_positions += c

        return min_eval, min_pos, evaluated_positions


# Min Max with Alpha Beta Pruning
def min_max_pruning(tictactoe: TicTacToe, alpha=-math.inf, beta=+math.inf, maximizing_player=True, player='X'):
    if tictactoe.game_over:
        return tictactoe.score(player), None, 1

    if maximizing_player:
        max_eval, max_pos, evaluated_positions = -math.inf, None, 0

        for pos in tictactoe.pending:
            new_tictactoe = tictactoe.copy()
            new_tictactoe.make_move(pos)
            cur_eval, _, c = min_max_pruning(new_tictactoe, alpha, beta, False, player)

            if max_eval < cur_eval:
                max_eval, max_pos = cur_eval, pos
            alpha = max(alpha, cur_eval)
            evaluated_positions += c
            if beta <= alpha:
                break

        return max_eval, max_pos, evaluated_positions

    else:
        min_eval, min_pos, evaluated_positions = +math.inf, None, 0
        for pos in tictactoe.pending:
            new_tictactoe = tictactoe.copy()
            new_tictactoe.make_move(pos)
            cur_eval, _, c = min_max_pruning(new_tictactoe, alpha, beta, True, player)
            if min_eval > cur_eval:
                min_eval, min_pos = cur_eval, pos
            beta = min(beta, cur_eval)
            if beta <= alpha:
                break

            evaluated_positions += c

        return min_eval, min_pos, evaluated_positions
