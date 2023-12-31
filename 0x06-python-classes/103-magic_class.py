#!/usr/bin/python3
"""Magic Class module"""
import math


class MagicClass:
    """MagicClass"""
    def __init__(self, radius=0):
        """intialization"""
        self.__radius = 0
        if (type(radius) is not int and type(radius) is not float):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """area method"""
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """circumference method"""
        return (2 * math.pi * self.__radius)
