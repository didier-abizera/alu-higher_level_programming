#!/usr/bin/python3
"""Module for safe_print_division function"""


def safe_print_division(a, b):
    """Divides 2 integers and prints the result"""
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
