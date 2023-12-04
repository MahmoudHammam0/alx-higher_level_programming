#!/usr/bin/python3
'''Geometry module'''


class BaseGeometry:
    '''class with non implemented area method'''
    def area(self):
        '''raise an exception message'''
        raise Exception('area() is not implemented')
