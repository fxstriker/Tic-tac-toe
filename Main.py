
# 0 NO PLAYER
# 1 X
# 2 O

game_over = False
player_x_turn = True
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]


# Loops valid win conditions checking if there is a win state
def win_condition():
    global game_over

    def check():
        global game_over
        if tempint == 3:
            print("X WINS")
            game_over = True
        elif tempint == 6:
            print("O WINS")
            game_over = True
    # TIE check
    spot_free = False
    for i in range(0, 3):
        for x in range(0, 3):
            if game[i][x] == 0:
                spot_free = True
    if spot_free is False:
        print("TIE")
        game_over = True

    # ROW check
    for i in range(0, 3):
        tempint = 0
        for x in range(0, 3):
            if game[i][x] == 0:
                tempint = 100
            tempint = tempint + (game[i][x])
        check()

    # COL check
    for i in range(0, 3):
        tempint = 0
        for x in range(0, 3):
            if game[x][i] == 0:
                tempint = 100
            tempint = tempint + (game[x][i])
        check()

    # daig checks
    tempint = 0
    for i in range(0, 3):
        if game[i][i] == 0:
            tempint = 100
        tempint = tempint + (game[i][i])
    check()

    tempint = 0
    for i in range(2, -1, -1):
        if game[i][i] == 0:
            tempint = 100
        tempint = tempint + (game[i][i])
    check()


def grid():
    draw = [" ", "X", "O"]
    line = "  --- --- ---"
    print("   1   2   3 ")
    print(line)
    write = "| "
    for colnum in range(0, 3):
        for i in range(0, 3):
            temp = game[colnum][i]
            write = write + (draw[temp] + " | ")
        print(str(colnum+1) + write + "\n" + line)
        write = "| "


def player_turn():
    global player_x_turn
    player_x_turn = not player_x_turn


def get_player_input():
    if player_x_turn is True:
        print("Player X turn")
    else:
        print("Player 0 turn")
    input_row = input("Input move as Column: ")
    input_column = input("Input move as Row: ")
    try:
        if game[int(input_row) - 1][int(input_column) - 1] == 0:
            if player_x_turn is True:
                game[int(input_row)-1][int(input_column)-1] = 1
            else:
                game[int(input_row)-1][int(input_column)-1] = 2
            player_turn()
        else:
            print("Invalid input re-enter turn")
            get_player_input()
    except ValueError:
        print("Invalid input re-enter turn")
        get_player_input()


while game_over is False:
    grid()
    win_condition()
    get_player_input()
