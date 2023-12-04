#!/usr/bin/python3
'''Only sub class of module'''


def inherits_from(obj, a_class):
    '''check if the object is an instance of a class inherited from a_class

    Args:
        obj: object to be checked
        a_class: class to check

    Return:
        True: if it was a sub class
        False: otherwise
    '''
    if isinstance(obj, a_class) and issubclass(type(obj), a_class):
        return True
    return False
