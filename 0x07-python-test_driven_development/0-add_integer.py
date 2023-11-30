#!/usr/bin/python3
'''

module for add_integer function

'''


def add_integer(a, b=98):
    '''
    simple functions that returns sum of two ints
    '''
    if type(a) not in [float, int]:
        raise TypeError('a must be an integer')
    if type(b) not in [float, int]:
        raise TypeError('b must be an integer')
    a = int(a)
    b = int(b)
    return (a + b)
