#!/usr/bin/python3
"""Module that defines append_write function"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file
    and returns number of characters added"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
