#!/usr/bin/python3
"""Module for matrix_divided function."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.

    Args:
        matrix: list of lists of integers/floats
        div: number to divide by
    """
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix) or not all(
            isinstance(el, (int, float))
            for row in matrix for el in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(el / div, 2) for el in row] for row in matrix]
