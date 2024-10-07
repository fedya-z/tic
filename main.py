board = [[' ' for _ in range(3)] for _ in range(3)]


def display_board():
    print("  0   1   2")
    for i, row in enumerate(board):
        print(i, ' | '.join(row))
        if i < 2:
            print("  ---|---|---")


def check_winner(player):
    for row in board:
        if row.count(player) == 3:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False


def check_draw():
    for row in board:
        if ' ' in row:
            return False
    return True


def is_valid_move(row, col):
    return 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' '


def tic_tac_toe():
    current_player = 'X'
    while True:
        display_board()
        print(f"Ход игрока {current_player}")

        move_valid = False
        while not move_valid:
            move = input("Введите строку и столбец через пробел (например: 1 2): ").split()

            if len(move) == 2 and move[0].isdigit() and move[1].isdigit():
                row, col = int(move[0]), int(move[1])
                if is_valid_move(row, col):
                    move_valid = True
                else:
                    print("Некорректный ход. Попробуйте снова.")
            else:
                print("Введите два числа от 0 до 2 через пробел.")

        board[row][col] = current_player

        if check_winner(current_player):
            display_board()
            print(f"Игрок {current_player} победил!")
            break

        if check_draw():
            display_board()
            print("Ничья!")
            break

        current_player = 'O' if current_player == 'X' else 'X'


tic_tac_toe()
