#!/usr/bin/python3
'''The N queens puzzle'''

import sys


def the_board(n):
    '''make a N×N chessboard'''
    new_board = []
    [new_board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in new_board]
    return (new_board)


def board_copy(new_board):
    '''make a copy of the board'''
    if isinstance(new_board, list):
        return list(map(board_copy, new_board))
    return (new_board)


def get_result(board):
    '''return result board'''
    res = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == "Q":
                res.append([row, col])
                break
    return (res)


def xcells(board, row, col):
    '''xout cells from the board'''
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


def solution(board, row, q, res):
    '''solve N queen puzzle by recursion'''
    if q == len(board):
        res.append(get_result(board))
        return (res)

    for col in range(len(board)):
        if board[row][col] == " ":
            tmp_board = board_copy(board)
            tmp_board[row][col] = "Q"
            xcells(tmp_board, row, col)
            res = solution(tmp_board, row + 1, q + 1, res)
    return (res)


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

    board = the_board(int(sys.argv[1]))
    res = solution(board, 0, 0, [])
    for sol in res:
        print(sol)
