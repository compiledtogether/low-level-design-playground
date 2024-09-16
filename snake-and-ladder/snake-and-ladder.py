import random

class TextColor:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'  # Reset to default color

class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self, steps):
        self.position += steps

    def update_position(self, new_position):
        self.position = new_position

    def __str__(self):
        return f"{TextColor.YELLOW}{self.name} is at position {self.position}"


class Board:
    def __init__(self, size):
        self.size = size
        self.snakes = {}
        self.ladders = {}

    def add_snake(self, start, end):
        self.snakes[start] = end

    def add_ladder(self, start, end):
        self.ladders[start] = end

    def get_new_position(self, position):
        if position in self.snakes:
            print(f"{TextColor.RED}Oops! Snake at {position}, going down to {self.snakes[position]}")
            return self.snakes[position]
        if position in self.ladders:
            print(f"{TextColor.GREEN}Yay! Ladder at {position}, going up to {self.ladders[position]}")
            return self.ladders[position]
        return position
    
    def display_board(self, players):
        board = [str(i).zfill(2) for i in range(1, self.size + 1)]

        # Add snakes and ladders symbols
        for start, end in self.snakes.items():
            board[start - 1] = f"S{str(start).zfill(2)}-{str(end).zfill(2)}"

        for start, end in self.ladders.items():
            board[start - 1] = f"L{str(start).zfill(2)}-{str(end).zfill(2)}"

        # Add players' positions
        for player in players:
            board[player.position - 1] = f"P{player.name[0].upper()}"
        
        # Display the board in a 10x10 grid
        print("\nCurrent Board:")
        for row in range(9, -1, -1):
            if row % 2 == 0:
                print(" -> ".join(board[row * 10: (row + 1) * 10]))
            else:
                print(" -> ".join(board[row * 10: (row + 1) * 10][::-1]))
        print()


class Game:
    def __init__(self, players, board):
        self.players = players
        self.board = board
        self.current_turn = 0

    def roll_dice(self):
        return random.randint(1, 6)

    def play_turn(self):
        player = self.players[self.current_turn]
        print(f"{TextColor.MAGENTA}{player.name}'s turn.")
        dice_value = self.roll_dice()
        print(f"{TextColor.BLUE}Rolled a {dice_value}")

        player.move(dice_value)
        
        if player.position > self.board.size:
            player.update_position(self.board.size)

        new_position = self.board.get_new_position(player.position)
        player.update_position(new_position)

        print(player)
        self.board.display_board(self.players)  # Show the board after each turn
        
        if self.is_winner(player):
            print(f"{TextColor.CYAN}{player.name} wins!")
            return True

        self.current_turn = (self.current_turn + 1) % len(self.players)
        return False

    def is_winner(self, player):
        return player.position == self.board.size

    def start(self):
        while True:
            if self.play_turn():
                break


# Initialize the game
board = Board(100)

# Adding some snakes
board.add_snake(14, 7)
board.add_snake(30, 10)
board.add_snake(84, 65)
board.add_snake(99, 78)

# Adding some ladders
board.add_ladder(3, 22)
board.add_ladder(5, 8)
board.add_ladder(20, 29)
board.add_ladder(27, 83)


player1 = input(f"{TextColor.YELLOW}Enter the name of player 1: ")
player2 = input(f"{TextColor.YELLOW}Enter the name of player 2: ")

players = [Player(player1), Player(player2)]

game = Game(players, board)

game.start()
