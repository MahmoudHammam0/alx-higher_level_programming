#!/usr/bin/python3
"""class Square that defines a square by its size"""


class Square:
    """class square with private attribute size"""
    def __init__(self, size=0, position=(0, 0)):
        """intialization"""
        self.size = size
        self.position = position

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

    def print_method(self):
        """printing square"""
        string = ""
        if (not self.__size):
            return ("\n")
        else:
            for n in range(self.__position[1]):
                string += "\n"
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    string += " "
                for j in range(self.__size):
                    string += "#"
                string += "\n"
        return (string)

    def my_print(self):
        """my_print mehod to print square"""
        print(self.print_method(), end="")

    def __str__(self):
        """print square class"""
        return (self.print_method()[:-1])
