#!/usr/bin/python3
"""Module for add_integer function."""


def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a: first integer
        b: second integer (default 98)
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
