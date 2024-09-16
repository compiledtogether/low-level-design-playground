# Snake and Ladder

Designing and implementing a Snake and Ladder game requires understanding both the game mechanics and how to structure the code efficiently. Below is a low-level design and a simple implementation in Python.

## Requirements

- Create a Snake and Ladder application.
- The application should take input n from the user.
- The game should have a board size of n x n.
- There should be n snakes and n ladders placed randomly in the board.
- Each snake will have its head at some number and its tail at a smaller number.
- Each ladder will have its start position at some number and end position at a larger number.
- There can be multiple players in the game.

### Rules
- The board has numbers from 1 to n^2.
- The players will make there move turn-by-turn.
- The game will have a six sided dice numbered from 1 to 6 and will always give a random number on rolling it.
- Each player has a piece which is initially kept outside the board (i.e., at position 0).
- Each player rolls the dice when their turn comes.
- Based on the dice value, the player moves their piece forward that number of cells. Ex: If the dice value is 4 and the player is at position 7, the player will move to position 11 (7+4).
- A player wins if he reached the last cell in the board.
- Whenever a player ends up at a cell with the head of the snake, the player should go down to the cell that has the tail of that snake.
- Whenever a player ends up at a cell with the start of the ladder, the player should go up to the cell that has the end of that ladder.
- The game should continue till there are at least 2 players still playing to win.
- After the dice roll, if a piece is supposed to move outside position 100, it does not move.
- Snakes and Ladders do not create a cycle.

## Low-Level Design

### Classes and Their Responsibilities:

### Player Class:

##### Attributes:
- name: The name of the player.
- position: The current position of the player on the board.

##### Methods:
- move(steps): Moves the player by a given number of steps.
- update_position(position): Updates the player's position based on snakes or ladders.

### Board Class:

##### Attributes:
- size: The total number of cells on the board (e.g., 100).
- snakes: A dictionary where keys are the starting points of snakes and values are the ending points.
- ladders: A dictionary where keys are the starting points of ladders and values are the ending points.

##### Methods:
- add_snake(start, end): Adds a snake to the board.
- add_ladder(start, end): Adds a ladder to the board.
- get_new_position(position): Returns the new position after checking for snakes or ladders.

### Game Class:

##### Attributes:
- players: A list of Player objects.
- board: A Board object.
- current_turn: Index of the player whose turn it is.

##### Methods:
- roll_dice(): Simulates rolling a dice (returns a random number between 1 and 6).
- play_turn(): Handles the logic for a player's turn.
- is_winner(player): Checks if the player has reached the final position.
- start(): Begins the game loop.


## Explanation

### Player Movement:

Each player starts at position 0. On each turn, they roll a dice to move forward.
After moving, their position is checked against the snakes and ladders. If they land on a snake's head, they move down to the snake's tail. If they land on a ladder's start, they climb to the ladder's end.

### Game Flow:

The game loop continues until a player reaches the final position on the board (size of the board, typically 100).
Board Setup:

The board is set up with snakes and ladders at predefined positions. These can be customized.

### Dice Rolling:

A simple random number generator simulates rolling a dice, returning a number between 1 and 6.

### Winner Determination:

The game checks after each turn if a player has reached the final position (100), declaring them the winner.

## Additional Enhancements (if needed):

### Handling Exact Position to Win:

Modify the code to require the player to land exactly on the final square to win.

### Multiple Players:

The code is designed to support multiple players, easily extendable by adding more Player objects to the players list.

### Edge Cases:

Handling when a player rolls a number that would take them past the final square (i.e., they do not move if the roll exceeds the target).