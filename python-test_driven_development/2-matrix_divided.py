#!/usr/bin/python3
"""
Module for matrix_divided function.

This module provides a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    Args:
        matrix: list of lists of integers/floats.
        div: number (int or float).

    Returns:
        A new matrix with each value divided by div (rounded to 2 decimals).

    Raises:
        TypeError: if matrix is invalid or div is not a number.
        ZeroDivisionError: if div is zero.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) "
            "of integers/floats"
        )

    row_length = len(matrix[0])

    new_matrix = []
    for row in matrix:
        if len(row) != row_length:
            raise TypeError(
                "Each row of the matrix must have the same size"
            )

        new_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) "
                    "of integers/floats"
                )
            new_row.append(round(element / div, 2))

        new_matrix.append(new_row)

    return new_matrix
