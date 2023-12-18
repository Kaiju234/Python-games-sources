#initialize the game board
# Initialize the game board
board = [[' ' for _ in range(7)] for _ in range(6)]

# Function to print the game board
def print_board(board):
    for row in board:
        print('|', end='')
        for cell in row:
            print(cell, end='|')
        print()
    print('---------------')
    print(' 1 2 3 4 5 6 7')

# Function to check if a player has won
def check_win(board, player):
    # Check rows
    for row in range(6):
        for col in range(4):
            if board[row][col] == board[row][col+1] == board[row][col+2] == board[row][col+3] == player:
                return True
    # Check columns
    for col in range(7):
        for row in range(3):
            if board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col] == player:
                return True
    # Check diagonals
    for row in range(3):
        for col in range(4):
            if board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3] == player:
                return True
    for row in range(3, 6):
        for col in range(4):
            if board[row][col] == board[row-1][col+1] == board[row-2][col+2] == board[row-3][col+3] == player:
                return True
    return False

# Function to check if the game is a draw
def check_draw(board):
    for row in board:
        if ' ' in row:
            return False
    return True

# Main game loop
current_player = 'X'
while True:
    # Print the board
    print_board(board)

    # Get the player's move
    column = int(input(f"Player {current_player}, choose a column (1-7): ")) - 1

    # Place the player's move on the board
    for row in range(5, -1, -1):
        if board[row][column] == ' ':
            board[row][column] = current_player
            break

    # Check for a win
    if check_win(board, current_player):
        print_board(board)
        print(f"Player {current_player} wins!")
        break

    # Check for a draw
    if check_draw(board):
        print_board(board)
        print("It's a draw!")
        break

    # Switch to the other player
    current_player = 'O' if current_player == 'X' else 'X'