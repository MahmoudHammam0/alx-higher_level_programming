#!/usr/bin/python3
'''Geometry module'''


class BaseGeometry:
    '''class with non implemented area method'''
    def area(self):
        '''raise an exception message'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''validate that value is int otherwise raise type and value errors'''
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
