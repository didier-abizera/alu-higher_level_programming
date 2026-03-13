#!/usr/bin/python3
"""Module for multiply_by_2 function"""


def multiply_by_2(a_dictionary):
    """Returns a new dictionary with all values multiplied by 2"""
    return {key: value * 2 for key, value in a_dictionary.items()}
