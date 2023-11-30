#!/usr/bin/python3
"""

multiplies 2 matrices module

"""


def matrix_mul(m_a, m_b):
    '''multiplies 2 matrices'''
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not all(isinstance(r, list) for r in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(r, list) for r in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_b == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_a == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not all((isinstance(idx, int) or isinstance(idx, float))
               for idx in [num for r in m_a for num in r]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(idx, int) or isinstance(idx, float))
               for idx in [num for r in m_b for num in r]):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(r) == len(m_a[0]) for r in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(r) == len(m_b[0]) for r in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    first_matrix = []
    for i in range(len(m_b[0])):
        row = []
        for j in range(len(m_b)):
            row.append(m_b[j][i])
        first_matrix.append(row)
    res_matrix = []
    for r in m_a:
        row = []
        for col in first_matrix:
            mul = 0
            for m in range(len(first_matrix[0])):
                mul += r[m] * col[m]
            row.append(mul)
        res_matrix.append(row)
    return res_matrix
