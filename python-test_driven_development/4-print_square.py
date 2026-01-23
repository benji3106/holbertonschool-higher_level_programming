#!/usr/bin/python3
"""Module that defines a function to print a square of a given size."""


def print_square(size):
    """Print a square of '#' characters of the given size."""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
