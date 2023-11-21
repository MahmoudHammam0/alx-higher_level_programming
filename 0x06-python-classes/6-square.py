#!/usr/bin/python3
"""class Square that defines a square by its size"""


class Square:
    """class square with private attribute size"""
    def __init__(self, size=0, position=(0, 0)):
        """intialization"""
        if (type(position) is not tuple or len(position) != 2
                or type(position[0]) is not int or type(position[1]) is not int
                or position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            self.__position = position

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

    @property
    def position(self):
        """getter method for position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """setter method for position"""
        self.__position = value

    def area(self):
        """calculate area of square"""
        res = (self.__size) ** 2
        return (res)

    def my_print(self):
        """print square with character '#'"""
        if (self.__size == 0):
            print()
        else:
            for i in range(self.__size):
                if i == 0:
                    for n in range(self.__position[1]):
                        print()
                for x in range(self.__position[0]):
                    print(" ", end='')
                for j in range(self.__size):
                    print("#", end='')
                print()
