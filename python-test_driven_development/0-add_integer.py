#!/usr/bin/python3
"""
Module for add_integer function.

This module provides a function that adds two integers.
"""


def add_integer(a, b=98):
    """Add two integers.

    Return the sum of a and b as an integer."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if isinstance(a, float):
        if a != a:
            raise TypeError("a must be an integer")
        if a == float('inf') or a == float('-inf'):
            raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(b, float):
        if b != b:
            raise TypeError("b must be an integer")
        if b == float('inf') or b == float('-inf'):
            raise TypeError("b must be an integer")

    return int(a) + int(b)
