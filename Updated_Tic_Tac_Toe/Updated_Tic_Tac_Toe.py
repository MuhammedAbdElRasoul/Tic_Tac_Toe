def print_board(board):
    # Number the game table and draw edges
    print("---------")
    for row in range(3):
        print("|", end="")
        for col in range(3):
            if board[row][col] == "":
                print(" " + str(col) + " |", end="")
            else:
                print(" " + board[row][col] + " |", end="")
        print()
    print("---------")

def handle_move(board, player):
    while True:
        row = int(input("Enter the row number (0-2): "))
        col = int(input("Enter the column number (0-2): "))
        if board[row][col] == "":
            board[row][col] = player
            break
        else:
            print("Invalid move! Try again.")

def check_win(board, player):
    # Check rows
    for row in board:
        if row.count(player) == 3:
            return True
    # Check columns
    for col in range(3):
        if [board[row][col] for row in range(3)].count(player) == 3:
            return True
    # Check diagonals
    if [board[i][i] for i in range(3)].count(player) == 3:
        return True
    if [board[i][2-i] for i in range(3)].count(player) == 3:
        return True
    return False

def check_tie(board):
    for row in board:
        if "" in row:
            return False
    return True

def play_again():
    # Ask player if they want to play again or not
    play_again = input("Do you want to play again (Y/N)? ").upper()
    if play_again == "Y":
        play_game()

def play_game():
    board = [[""] * 3 for _ in range(3)]
    players = ["X", "O"]
    print("Welcome to Tic Tac Toe!")

    # Ask player what they want to play with: X or O
    player = input("Do you want to play with X or O? ").upper()
    if player == "X" :
        current_player = 0
    elif player == "O" :
        current_player = 1   
    else :
        print("Invalid choice! Please choose X or O.")
        play_game()

    while True:
        print_board(board)

        handle_move(board, player)
        if check_win(board, player):
            print_board(board)
            print("Player", player, "wins!")
            play_again()
            break

        elif check_tie(board):
            print_board(board)
            print("It's a tie!")
            play_again()
            break

        current_player = (current_player + 1) % 2
        player = players[current_player]

play_game()