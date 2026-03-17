#!/usr/bin/python3
"""Module for Square class"""


class Square:
    """Class that defines a square by size with validation"""

    def __init__(self, size=0):
        """Instantiation with optional size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
