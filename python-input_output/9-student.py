#!/usr/bin/python3
"""Module that defines a Student class."""


class Student:
    """Define a student with basic attributes."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return the dictionary representation of a Student instance."""
        return self.__dict__
