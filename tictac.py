class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 1

    def print_board(self):
        for i in range(3):
            print(" | ".join(self.board[i]))
            if i < 2:
                print("---------")

    def make_move(self, row, col):
        if row < 0 or row >= 3 or col < 0 or col >= 3 or self.board[row][col] != ' ':
            return False
        self.board[row][col] = 'X' if self.current_player == 1 else 'O'
        self.current_player = 3 - self.current_player
        return True

    def is_board_full(self):
        return all(cell != ' ' for row in self.board for cell in row)

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] != ' ' and self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return True
            if self.board[0][i] != ' ' and self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return True
        if self.board[0][0] != ' ' and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return True
        if self.board[0][2] != ' ' and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return True
        return False

    def get_current_player(self):
        return self.current_player


def main():
    game = TicTacToe()

    # Predefined moves (Player 1 wins)
    #moves = [(0, 0), (1, 1), (0, 1), (1, 0), (0, 2)]

    # for row, col in moves:
    while 1<2:
        row=int(input())
        col=int(input())
        game.print_board()
        print(f"Player {game.get_current_player()} plays ({row},{col})")
        game.make_move(row, col)
        if game.check_winner() or game.is_board_full():
            break

    game.print_board()
    if game.check_winner():
        print(f"Player {3 - game.get_current_player()} wins!")
    else:
        print("It's a draw!")


if __name__ == "__main__":
    main()