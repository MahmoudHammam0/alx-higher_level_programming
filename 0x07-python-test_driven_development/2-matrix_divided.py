#!/usr/bin/python3
'''

matrix division module

'''


def matrix_divided(matrix, div):
    '''Return a new matrix after divides all elements of a matrix.

    Args:
        matrix: list of lists of integers or floats
        div: integer or float which divide the matrix

    Return:
        new matrix after division

    Raises:
        TypeError: if matrix wasn't list of lists of the same size
        TypeError: if div not an integer or float
        ZeroDivisionError: if div is 0
    '''
    new_matrix = []
    err = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(err)
    if type(div) not in [int, float, 0]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    length = len(matrix[0])
    for row in matrix:
        new_list = []
        if type(row) is not list or len(row) == 0:
            raise TypeError(err)
        if len(row) != length:
            raise TypeError('Each row of the matrix must have the same size')
        for i in range(len(row)):
            if type(row[i]) not in [int, float]:
                raise TypeError(err)
            new_list.append(round(row[i] / div, 2))
        new_matrix.append(new_list)
    return new_matrix
