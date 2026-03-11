#!/usr/bin/python3
def multiple_returns(sentence):
    """Returns a tuple with length and first character of a string"""
    if len(sentence) == 0:
        return (0, None)
    return (len(sentence), sentence[0])
