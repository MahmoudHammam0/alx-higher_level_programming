#!/usr/bin/python3
'''locked class module'''


class LockedClass:
    '''locked class only accept first_name as attribute'''
    __slots__ = ['first_name']
