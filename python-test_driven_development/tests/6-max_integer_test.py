#!/usr/bin/python3
"""Unittest for max_integer([..]).
This module contains test cases for the max_integer function.
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_ordered_list(self):
        """Max at the end of an ordered list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Max in the middle of an unordered list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        """List with all negative numbers."""
        self.assertEqual(max_integer([-1, -3, -2, -10]), -1)

    def test_mixed_numbers(self):
        """List with positive and negative numbers."""
        self.assertEqual(max_integer([-5, 0, 5, 3]), 5)

    def test_one_element_list(self):
        """List with only one element."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """Calling function with no argument uses default empty list."""
        self.assertIsNone(max_integer())


if __name__ == '__main__':
    unittest.main()
