#!/usr/bin/python3
'''

Lazy matrix multiplication module

'''

import numpy


def lazy_matrix_mul(m_a, m_b):
    '''matrix multiplication using Numpy module'''
    return numpy.matmul(m_a, m_b)
