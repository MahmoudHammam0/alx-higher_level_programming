#!/usr/bin/python3
"""class Square that defines a square by its size"""


class Square:
    """class square with private attribute size"""
    def __init__(self, size=0, position=(0, 0)):
        """intialization"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """getter method for size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter method for size"""
        if (not isinstance(value, int)):
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
        if (not isinstance(value, tuple)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (not isinstance(value[0], int) or not isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """calculate area of square"""
        res = (self.__size) ** 2
        return (res)

    def my_print(self):
        """printing square"""
        if (not self.__size):
            print()
        else:
            for n in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end='')
                for j in range(self.__size):
                    print("#", end='')
                print()

    def __str__(self):
        """print square class"""
        new_str = ""
        if (not self.__size):
            return ("\n")
        else:
            for n in range(self.__position[1]):
                new_str += "\n"
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    new_str += " "
                for j in range(self.__size):
                    new_str += "#"
                new_str += "\n"
        return (new_str[:-1])
