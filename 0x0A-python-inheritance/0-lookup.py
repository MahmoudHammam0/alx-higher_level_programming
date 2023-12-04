#!/usr/bin/python3
'''Lookup method module'''


def lookup(obj):
    '''returns the list of available attributes and methods of an object

    Args:
        obj: object to return its attributes and methods

    Return:
        returns the list of available attributes and methods of an object
    '''
    return dir(obj)
