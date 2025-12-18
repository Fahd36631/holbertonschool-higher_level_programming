#!/usr/bin/python3
"""Defines a class that inherits from list and prints it sorted."""


class MyList(list):
    """Custom list class that can print its elements sorted."""

    def print_sorted(self):
        """Prints the list sorted in ascending order and returns it."""
        sorted_list = sorted(self)
        print(sorted_list)
        return sorted_list
