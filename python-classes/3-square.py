#!/usr/bin/python3
"""Module that defines a Square class with area computation."""


class Square:
    """Class that defines a square."""

    def __init__(self, size=0):
        """Initialize a new square with validated size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size
