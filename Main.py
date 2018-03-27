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
            # TODO FIX DIAG CHECK FROM LEFT UP TO RIGHT
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
    print("    A   B   C ")
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
    alpha_to_int = {"a": "1", "b": "2", "c": "3"}
    assert 0 <= player < 2, "Player must be 0 or 1"
    print("Player %s turn" % PLAYER_LABELS[player + 1])
    test = 0
    while test == 0:
        try:
            value = input("Input move as cords example A1 : ")
            if len(value) == 2 and value[0].isalpha() and value[1].isdigit():
                test = 1
                input_row = int(value[1]) - 1
                if value[0].lower() in alpha_to_int.keys():
                    input_column = int(alpha_to_int[value[0].lower()]) - 1
                else:
                    print("You must enter a valid coordinate with a range of A - C for example A1")
                    test = 0
                    input_column = 0
            else:
                test = 0
                print("You must enter a valid coordinate with a range of A - C / 1 - 3  for example A1")
            if input_row < 0 or input_row > 2 or input_column < 0 or input_column > 2:
                test = 0
                print("You must enter a valid coordinate with a range of 1 - 3  for example A1")
        except ValueError:
            test = 0
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
    print_grid(game_grid)
    current_player, game_grid = get_player_input(game_grid, current_player)
    winner = win_condition(game_grid)

# Print the result
print_grid(game_grid)
if winner < 3:
    print("Player %s wins!" % PLAYER_LABELS[winner])
else:
    print("Draw!")