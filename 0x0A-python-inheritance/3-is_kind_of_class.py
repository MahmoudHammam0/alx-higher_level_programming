#!/usr/bin/python3
'''Same class or inherit from module'''


def is_kind_of_class(obj, a_class):
    '''check if obj is an instance of or inherited from a_class

    Args:
        obj: object to be checked
        a_class: class to check

    Return:
        True: if it was an instance or inherited
        False: otherwise
    '''
    if isinstance(obj, a_class):
        return True
    return False
