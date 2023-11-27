#!/usr/bin/python3
'''The N queens puzzle'''

import sys


def new_board(n):
    '''make new board of size nXn'''
    n_board = []
    [n_board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in n_board]
    return (n_board)


def board_copy(t_board):
    '''return a copy of the board'''
    if isinstance(t_board, list):
        return list(map(board_copy, t_board))
    return (t_board)


def get_result(a_board):
    '''return solved board'''
    result = []
    for row in range(len(a_board)):
        for col in range(len(a_board)):
            if board[row][col] == "Q":
                result.append([row, col])
                break
    return (result)


def xout(board, row, col):
    '''x out cells of the board'''
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def recursive_solve(board, row, queens, solutions):
    '''solve n queens puzzle with recursion'''
    if queens == len(board):
        solutions.append(get_result(board))
        return (solutions)

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = board_copy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = new_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
