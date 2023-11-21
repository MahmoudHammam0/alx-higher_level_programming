#!/usr/bin/python3
"""class Square that defines a square by its size"""


class Square:
    """class square with private attribute size"""
    def __init__(self, size=0):
        """intialization"""
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            self.comp = self.area()

    @property
    def size(self):
        """getter method for size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter method for size"""
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """calculate area of square"""
        res = (self.__size) ** 2
        return (res)

    def __lt__(self, other):
        """less than comparsion"""
        return (self.comp < other.comp)

    def __gt__(self, other):
        """greater than comparsion"""
        return (self.comp > other.comp)

    def __eq__(self, other):
        """equal to comparsion"""
        return (self.comp == other.comp)

    def __le__(self, other):
        """less than or equal to comparsion"""
        return (self.comp <= other.comp)

    def __ge__(self, other):
        """greater than or equal to comparsion"""
        return (self.comp >= other.comp)

    def __ne__(self, other):
        """not equal to comparsion"""
        return (self.comp != other.comp)
