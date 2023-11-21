#!/usr/bin/python3
"""Magic Class module"""

import math


class MagicClass:
    """MagicClass"""
    def __init__(self, radius):
        """intialization"""
        if (type(radius) is not int or type(radius) is not float):
            raise TypeError("radius must be a number")
        self.radius = radius

    def area(self):
        """area method"""
        return ((2 ** self.radius) * math.pi)

    def circumference(self):
        """circumference method"""
        return (2 * math.pi * self.radius)
