#!/usr/bin/python3
'''

print square module

'''


def print_square(size):
    '''print square with character '#'

    Args:
        size: length of the square
    return:
        Nothing
    Raises:
        TypeError: size must be an integer
        ValueError: size less than 0
    '''
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if type(size) is float and size < 0:
        raise TypeError('size must be an integer')
    for line in range(size):
        for row in range(size):
            print("#", end='')
        print()
