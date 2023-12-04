#!/usr/bin/python3
'''Rectangle module that inherits from basegeometry'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''class Rectangle inherits from basegeometry'''
    def __init__(self, width, height):
        '''initialization'''
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
