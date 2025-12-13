#!/usr/bin/python3
"""Module that defines a Square class
"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Initialize the square with a size"""
        self.size = size

    @property
    def size(self):
        """Getter: retrieve the private attribute size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter: validate and update the private attribute size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#'"""
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__size):
            print("#" * self.__size)
