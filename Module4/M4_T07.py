from random import randrange


def display_board(board):
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print("|   " + "   |   ".join(str(x) for x in row) + "   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")


def make_list_of_free_fields(board):
    free_fields = []
    for row in range(3):
        for col in range(3):
            if isinstance(board[row][col], int):
                free_fields.append(board[row][col])
    return free_fields


def enter_move(board):
    free_fields = make_list_of_free_fields(board)
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move in free_fields:
                for row in range(3):
                    for col in range(3):
                        if board[row][col] == move:
                            board[row][col] = 'O'
                return
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Please enter a valid number.")


def victory_for(board, sign):
    for i in range(3):
        if all(board[i][j] == sign for j in range(3)) or all(board[j][i] == sign for j in range(3)):
            return True
    if board[0][0] == board[1][1] == board[2][2] == sign or board[0][2] == board[1][1] == board[2][0] == sign:
        return True
    return False


def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    move = free_fields[randrange(len(free_fields))]
    for row in range(3):
        for col in range(3):
            if board[row][col] == move:
                board[row][col] = 'X'
                return


def main():
    board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]
    display_board(board)

    while True:
        enter_move(board)
        display_board(board)
        if victory_for(board, 'O'):
            print("You won!")
            break
        if not make_list_of_free_fields(board):
            print("It's a tie!")
            break

        draw_move(board)
        display_board(board)
        if victory_for(board, 'X'):
            print("Computer won!")
            break
        if not make_list_of_free_fields(board):
            print("It's a tie!")
            break


main()
