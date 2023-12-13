import random
import os
from msvcrt import getch  # for Windows

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    clear_screen()
    for row in board:
        print(" ".join(map(str, row)))

def initialize_board():
    board = [[0] * 4 for _ in range(4)]
    add_new_tile(board)
    return board

def add_new_tile(board):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = random.choice([2, 4])

def move_left(board):
    for i in range(4):
        board[i] = merge_tiles(board[i])
    add_new_tile(board)

def move_right(board):
    for i in range(4):
        board[i] = merge_tiles(board[i][::-1])[::-1]
    add_new_tile(board)

def move_up(board):
    for j in range(4):
        column = [board[i][j] for i in range(4)]
        merged_column = merge_tiles(column)
        for i in range(4):
            board[i][j] = merged_column[i]
    add_new_tile(board)

def move_down(board):
    for j in range(4):
        column = [board[i][j] for i in range(3, -1, -1)]
        merged_column = merge_tiles(column)
        for i in range(3, -1, -1):
            board[i][j] = merged_column.pop()
    add_new_tile(board)

def merge_tiles(line):
    merged_line = [0] * 4
    current_index = 0

    for value in line:
        if value != 0:
            if merged_line[current_index] == 0:
                merged_line[current_index] = value
            elif merged_line[current_index] == value:
                merged_line[current_index] *= 2
                current_index += 1
            else:
                current_index += 1
                merged_line[current_index] = value

    return merged_line

def check_game_over(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return False

    for i in range(4):
        for j in range(3):
            if board[i][j] == board[i][j + 1] or board[j][i] == board[j + 1][i]:
                return False

    return True

def main():
    board = initialize_board()
    print_board(board)

    while not check_game_over(board):
        key = ord(getch())
        if key == 224:  # arrow key
            key = ord(getch())
            if key == 75:  # left arrow
                move_left(board)
            elif key == 77:  # right arrow
                move_right(board)
            elif key == 72:  # up arrow
                move_up(board)
            elif key == 80:  # down arrow
                move_down(board)
            print_board(board)

    print("Game Over!")

if __name__ == "__main__":
    main()
