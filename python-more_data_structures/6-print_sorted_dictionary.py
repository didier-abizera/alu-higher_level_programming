#!/usr/bin/python3
"""Module for print_sorted_dictionary function"""


def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys"""
    for key in sorted(a_dictionary):
        print("{}: {}".format(key, a_dictionary[key]))
