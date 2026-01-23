#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_sorted_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unsorted_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-10, -3, -50, -1]), -1)

    def test_mixed_int_float(self):
        self.assertEqual(max_integer([1, 2.5, 3, 0.2]), 3)

    def test_all_floats(self):
        self.assertEqual(max_integer([1.1, 2.2, 0.5]), 2.2)

    def test_duplicates(self):
        self.assertEqual(max_integer([2, 2, 2]), 2)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([9, 1, 2, 3]), 9)

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 9]), 9)

    def test_string_list(self):
        # Works because strings are comparable in Python
        self.assertEqual(max_integer(["a", "z", "b"]), "z")

    def test_type_error_mixed_incomparable(self):
        with self.assertRaises(TypeError):
            max_integer([1, "2", 3])


if __name__ == "__main__":
    unittest.main()
