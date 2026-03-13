#!/usr/bin/python3
"""Module for best_score function"""


def best_score(a_dictionary):
    """Returns a key with the biggest integer value"""
    if not a_dictionary:
        return None
    return max(a_dictionary, key=lambda k: a_dictionary[k])
