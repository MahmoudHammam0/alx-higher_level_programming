#!/usr/bin/python3
'''class Square module'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''class Square inherits from Rectnagle'''
    def __init__(self, size, x=0, y=0, id=None):
        '''initialization'''
        self.size = size
        self.x = x
        self.y = y
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''getter for size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''setter for size'''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value
        self.__height = value
        self.__size = value

    def __str__(self):
        '''overrides the Rectangle str method'''
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.size)
