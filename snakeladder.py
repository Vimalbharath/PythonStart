import random

class GamePlayer:
    """Encapsulates a player properties"""

    def __init__(self, _id):
        self._id = _id
        self.rank = -1        # initial dummy rank
        self.position = 1     # starting position

    def set_position(self, pos):
        self.position = pos

    def set_rank(self, rank):
        self.rank = rank

    def get_pos(self):
        return self.position

    def get_rank(self):
        return self.rank


class MovingEntity:
    """
    Base class for moving entities like Snake, Ladder, Wormhole, etc.
    """

    def __init__(self, end_pos=None):
        self.end_pos = end_pos
        self.desc = None

    def set_description(self, desc):
        self.desc = desc

    def get_end_pos(self):
        if self.end_pos is None:
            raise Exception("no_end_position_defined")
        return self.end_pos


class Snake(MovingEntity):
    def __init__(self, end_pos=None):
        super().__init__(end_pos)
        self.desc = "Bit by Snake"


class Ladder(MovingEntity):
    def __init__(self, end_pos=None):
        super().__init__(end_pos)
        self.desc = "Climbed Ladder"


class Board:
    """Game board with size and moving entities"""

    def __init__(self, size):
        self.size = size
        self.board = {}  # map of {pos: MovingEntity}

    def get_size(self):
        return self.size

    def set_moving_entity(self, pos, moving_entity):
        self.board[pos] = moving_entity

    def get_next_pos(self, player_pos):
        if player_pos > self.size:
            return player_pos
        if player_pos not in self.board:
            return player_pos
        print(f'{self.board[player_pos].desc} at {player_pos}')
        return self.board[player_pos].get_end_pos()

    def at_last_pos(self, pos):
        return pos == self.size


class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)


class Game:
    def __init__(self):
        self.board = None
        self.dice = None
        self.players = []
        self.turn = 0
        self.last_rank = 0
        self.consecutive_six = 0

    def initialize_game(self, board: Board, dice_sides, players_count):
        self.board = board
        self.dice = Dice(dice_sides)
        self.players = [GamePlayer(i) for i in range(players_count)]

    def can_play(self):
        return self.last_rank != len(self.players)

    def get_next_player(self):
        while True:
            if self.players[self.turn].get_rank() == -1:
                return self.players[self.turn]
            self.turn = (self.turn + 1) % len(self.players)

    def move_player(self, curr_player, next_pos):
        curr_player.set_position(next_pos)
        if self.board.at_last_pos(curr_player.get_pos()):
            curr_player.set_rank(self.last_rank + 1)
            self.last_rank += 1

    def can_move(self, curr_player, to_move_pos):
        return to_move_pos <= self.board.get_size() and curr_player.get_rank() == -1

    def change_turn(self, dice_result):
        self.consecutive_six = 0 if dice_result != 6 else self.consecutive_six + 1
        if dice_result != 6 or self.consecutive_six == 3:
            if self.consecutive_six == 3:
                print("Changing turn due to 3 consecutive sixes")
            self.turn = (self.turn + 1) % len(self.players)
        else:
            print(f"One more turn for player {self.turn+1} after rolling 6")

    def play(self):
        while self.can_play():
            curr_player = self.get_next_player()

            # ✅ No input required
            dice_result = self.dice.roll()
            print(f"\nPlayer {self.turn+1} rolled -> {dice_result}")

            _next_pos = self.board.get_next_pos(curr_player.get_pos() + dice_result)
            if self.can_move(curr_player, _next_pos):
                self.move_player(curr_player, _next_pos)

            self.change_turn(dice_result)
            self.print_game_state()
            next=input("Roll a die : ")
            if not next:
                break

        self.print_game_result()

    def print_game_state(self):
        print('-------------game state-------------')
        for ix, _p in enumerate(self.players):
            print(f'Player {ix+1} is at pos {_p.get_pos()} (Rank: {_p.get_rank()})')
        print('-----------------------------------\n')

    def print_game_result(self):
        print('-------------final result-------------')
        for _p in sorted(self.players, key=lambda x: x.get_rank()):
            print(f'Player: {_p._id+1} , Rank: {_p.get_rank()}')


def sample_run():
    board = Board(30)  # bigger board for fun
    board.set_moving_entity(14, Snake(7))
    board.set_moving_entity(25, Snake(5))
    board.set_moving_entity(3, Ladder(22))
    board.set_moving_entity(11, Ladder(28))

    game = Game()
    game.initialize_game(board, 6, 4)  # 2 players
    game.play()


if __name__ == "__main__":
    sample_run()