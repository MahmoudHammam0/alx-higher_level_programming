#!/usr/bin/python3
'''Square #1 module'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''class square inherits from Rectangle'''
    def __init__(self, size):
        '''initialization'''
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        '''calculate area of square'''
        return self.__size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
