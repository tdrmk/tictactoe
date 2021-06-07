from __future__ import annotations


class TicTacToe:
    def __init__(self):
        self.state = {
            (0, 0): '', (1, 0): '', (2, 0): '',
            (0, 1): '', (1, 1): '', (2, 1): '',
            (0, 2): '', (1, 2): '', (2, 2): '',
        }
        self.turn = 'X'

    def __str__(self):
        return f'{self.state[0, 0]:1}|{self.state[1, 0]:1}|{self.state[2, 0]:1}\n' + \
               f'{self.state[0, 1]:1}|{self.state[1, 1]:1}|{self.state[2, 1]:1}\n' + \
               f'{self.state[0, 2]:1}|{self.state[1, 2]:1}|{self.state[2, 2]:1}\n'

    def make_move(self, pos):
        if not self.state[pos]:
            self.state[pos] = self.turn
            self.turn = 'O' if self.turn == 'X' else 'X'

    def score(self, player):
        # Returns 1 if player won, -1 if lost
        return 1 if self.winner == player else 0 if self.winner == '' else -1
    
    @property
    def game_over(self):
        # either if winner found or no more positions to fill
        return self.winner or all(self.state[pos] for pos in self.state)

    @property
    def winner(self):
        for i in range(3):
            if self.state[i, 0] == self.state[i, 1] == self.state[i, 2]:
                return self.state[i, 0]

        for j in range(3):
            if self.state[0, j] == self.state[1, j] == self.state[2, j]:
                return self.state[0, j]

        if self.state[0, 0] == self.state[1, 1] == self.state[2, 2]:
            return self.state[0, 0]

        if self.state[2, 0] == self.state[1, 1] == self.state[0, 2]:
            return self.state[2, 0]

        return 'Draw'

    @property
    def pending(self):
        return [pos for pos in self.state if self.state[pos] == '']

    def copy(self) -> TicTacToe:
        new = TicTacToe()
        new.state = {
            (0, 0): self.state[0, 0], (1, 0): self.state[1, 0], (2, 0): self.state[2, 0],
            (0, 1): self.state[0, 1], (1, 1): self.state[1, 1], (2, 1): self.state[2, 1],
            (0, 2): self.state[0, 2], (1, 2): self.state[1, 2], (2, 2): self.state[2, 2],
        }
        new.turn = self.turn
        return new
