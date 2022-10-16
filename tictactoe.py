board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]


def print_board(board):
    for row in board:
        for cell in row:
            print('[' + str(cell) + ']', end='')
        print()
    print()
    print()


def get_input():
    s = input("Enter a cell:")
    s = str(s)
    return s


# 'valid'input is a letter from a to c representing
# a row, and a number from 1-3 representing a column
def is_valid_input(s):
    # verify correct input length & that the row/col exist
    if len(s) != 2:
        return False
    if s[0] not in ('a', 'b', 'c'):
        return False
    if int(s[1]) < 1 or int(s[1]) > 3:
        return False

    # check the cell hasn't been chosen before
    if not is_free_cell(s):
        return False

    return True


def is_free_cell(s):
    s = input_to_indices(s)
    r = int(s[0])
    c = int(s[1])

    if board[r][c] != ' ': return False
    return True


def input_to_indices(player_input):
    row = player_input[0]

    if row == 'a': row = 0
    elif row == 'b': row = 1
    elif row == 'c': row = 2

    column = player_input[1]
    column = int(column) - 1

    return str(row) + str(column)


def execute_player_choice(choice, player_num):
    # assumes valid input
    choice = input_to_indices(choice)

    row = int(choice[0])
    col = int(choice[1])

    if player_num == 1:
        board[row][col] = 'X'
    elif player_num == 2:
        board[row][col] = 'O'


def is_game_won(board, player):
    # player_mark = 'X'
    # if player == 2:
    #     player_mark = 'O'

    player_mark = 'X' if player == 1 else 'O'

    sequence = 0
    # check each row
    for row in board:
        for cell in row:
            if cell == player_mark:
                sequence += 1

        if sequence == 3:
            return True
        sequence = 0

    sequence = 0
    # check each column
    for i in range(3):
        for j in range(3):
            if board[j][i] == player_mark:
                sequence += 1

        if sequence == 3:
            return True
        sequence = 0

    sequence = 0

    # check both diagonals
    # top left to bottom right
    for i in range(3):
        if board[i][i] == player_mark:
            sequence += 1

    if sequence == 3:
        return True

    # top right to bottom left
    sequence == 0

    i = 0
    j = 2

    while i != 3 and j != 0:
        if board[i][j] == player_mark:
            sequence += 1

        i += 1
        j -= 1

    if sequence == 3:
        return True

    return False


def game():
    player = 1
    print_board(board)

    while True:
        print(f"It's Player {player}'s turn.")
        choice = input("Enter a cell: ")

        # check input is valid (if not, 'continue')
        if not is_valid_input(choice):
            print("Invalid row or column")
            # explain how to give valid input
            continue

        # modify board
        execute_player_choice(choice, player)

        # show board
        print_board(board)

        # if player won, break loop
        if (is_game_won(board, player)):
            print("Player", player, "won!")
            return

        # otherwise, change player
        if player == 1: player = 2
        elif player == 2: player = 1

    # show winner & end game


game()
