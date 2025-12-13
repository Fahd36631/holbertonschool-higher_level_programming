#!/usr/bin/python3
"""Module that defines a Square class with size and position
"""


class Square:
    """Defines a square with size and position"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size with validation"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position with validation"""
        if (
            type(value) is not tuple or
            len(value) != 2 or
            type(value[0]) is not int or
            type(value[1]) is not int or
            value[0] < 0 or
            value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Return area of square"""
        return self.__size ** 2

    def my_print(self):
        """Print square using '#' considering position"""
        if self.__size == 0:
            print("")
            return

        # position[1] = عدد الأسطر الفارغة فوق المربع
        for _ in range(self.__position[1]):
            print("")

        # طباعة الصفوف
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
