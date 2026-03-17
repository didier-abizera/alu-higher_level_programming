#!/usr/bin/python3
"""Module for MagicClass"""
import math


class MagicClass:
    """Class that does magic with radius"""

    def __init__(self, radius=0):
        """Instantiation with radius"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Returns the area"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Returns the circumference"""
        return 2 * math.pi * self.__radius
