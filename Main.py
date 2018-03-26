import numpy as np

# 0 NO PLAYER
# 1 X
# 2 O
PLAYER_LABELS = (' ', 'X', 'O')


def win_condition(grid):
    """
    Calculates the winner (if any) for a given game grid
    :param grid: the game grid
    :return: False if no winner, 1 or 2 for X or O, or 3 for draw
    """
    for player in (1, 2):
        player_positions = (grid == player)
        if player_positions.all(axis=0).any() or player_positions.all(axis=1).any() or np.diag(player_positions).all():
            return player
    if (grid != 0).all():
        return 3
    return False


def print_grid(grid):
    """
    Prints the game grid to screen (or other buffer if output is specified)
    :param grid: the current game grid
    """
    line = "   --- --- ---"
    print("    1   2   3 ")
    print(line)
    for row_num, row in enumerate(grid):
        print("%i " % (row_num + 1), end='')
        for item in row:
            print("| %s " % PLAYER_LABELS[item], end='')
        print("|")
        print(line)


def get_player_input(grid, player):
    """
    Gets the row/col input for the given player
    :param grid: the current game grid
    :param player: the player, either 1 or 2
    :return: the new game grid
    """
    assert 0 <= player < 2, "Player must be 0 or 1"

    def ask_value(name):
        value = 0
        while value == 0:
            try:
                value = int(input("Input move as %s: " % name))
            except ValueError:
                pass
            if value < 1 or value > 3:
                print("You must enter a number between 1 and 3")
                value = 0
        return value

    print("Player %s turn" % PLAYER_LABELS[player + 1])

    input_column = ask_value("column") - 1
    input_row = ask_value("row") - 1
    if grid[input_row, input_column] == 0:
        grid[input_row, input_column] = player + 1
    else:
        print("Position already taken! Try again.")
        return get_player_input(grid, player)

    next_player = (player + 1) % 2
    return next_player, grid


# Set up initial game state
game_grid = np.zeros((3, 3), dtype=np.int8)
current_player = 0
winner = False

# Loop until a winner is found
while not winner:
    current_player, game_grid = get_player_input(game_grid, current_player)
    print_grid(game_grid)
    winner = win_condition(game_grid)

# Print the result
if winner < 3:
    print("Player %s wins!" % PLAYER_LABELS[winner])
else:
    print("Draw!")