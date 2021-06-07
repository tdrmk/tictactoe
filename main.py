from tictaetoe import TicTacToe
from min_max import min_max_pruning
from random import choice

if __name__ == '__main__':
    t = TicTacToe()
    num_turns = 0
    # Game between two bots
    while not t.game_over:
        num_turns += 1

        if t.turn == 'X':
            # Min Max AI
            score, pos, count = min_max_pruning(t, maximizing_player=True, player='X')
            print(f"{num_turns} [MIN MAX] TURN:{t.turn}, SCORE:{score}, POS:{pos}, NODES:{count}")
            t.make_move(pos)
        else:
            # Random AI
            pos = choice(t.pending)
            t.make_move(pos)
            print(f"{num_turns} [RANDOM] TURN:{t.turn} POS:{pos}")
            # score, pos, count = min_max_pruning(t, maximizing_player=True, player='O')
            # print(f"{num_turns} [MIN MAX] TURN:{t.turn}, SCORE:{score}, POS:{pos}, NODES:{count}")
            # t.make_move(pos)

        print(t)

    print(f"Winner: {t.winner}")
