from typing import ValuesView


def Solution(board):
    Finder = emptyCell(board)
    if not Finder:
        return True
    else:
        row, col = Finder

    for i in range(1, 10):
        if chkValidity(board, i, (row, col)):
            board[row][col] = i

            if Solution(board):
                return True
            board[row][col] = 0
    return False


def chkValidity(board, num, pos):
    # * Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # * Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # * Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True  # * Returns if all is good


def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def emptyCell(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # * Row and Column
    return None
