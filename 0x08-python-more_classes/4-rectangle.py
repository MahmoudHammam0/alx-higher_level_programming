#!/usr/bin/python3
'''

module for class rectangle with width and height attributes

'''


class Rectangle:
    '''class rectangle with width and height attribute'''
    def __init__(self, width=0, height=0):
        '''initialization'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''property of width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''setter method for width'''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        '''property of height attribute'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter method for height attribute'''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        '''returns area of rectangle'''
        return self.__width * self.__height

    def perimeter(self):
        '''returns perimeter of rectangle'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        '''print rectangle with character "#"'''
        if self.__width == 0 or self.__height == 0:
            return ""
        new_str = ""
        for h in range(self.__height):
            for w in range(self.__width):
                new_str += "#"
            if h != self.__height - 1:
                new_str += "\n"
        return new_str

    def __repr__(self):
        ''' return a string used by eval to make instances'''
        new_str = ""
        repr_str = "Rectangle("
        for h in range(self.__height):
            for w in range(self.__width):
                new_str += "#"
            if h != self.__height - 1:
                new_str += "\n"
        return repr_str + str(self.__width) + ", " + str(self.__height) + ")"
