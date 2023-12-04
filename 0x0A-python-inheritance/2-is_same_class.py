#!/usr/bin/python3
'''Exact same object module'''


def is_same_class(obj, a_class):
    '''check if the obj is an instance of the a_class

    Args:
        obj: object to be checked
        a_class: class to check

    Return:
        True: if it was an instance
        False: otherwise
    '''
    if type(obj) == a_class:
        return True
    return False
