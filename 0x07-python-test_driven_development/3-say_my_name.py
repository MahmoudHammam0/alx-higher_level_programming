#!/usr/bin/python3
'''

Say My Name module

'''


def say_my_name(first_name, last_name=""):
    '''take first and last name (as strings) and return fullname

    Args:
        first_name: string of first name
        last_name: string of last name or empty string

    Return:
        fullname of first and last name compined

    Raises:
        TypeError: if first or last name not strings
    '''
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print("My name is {} {}".format(first_name, last_name))
