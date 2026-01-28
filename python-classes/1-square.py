#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """A class that defines a square with a private size attribute."""

    def __init__(self, size):
        """Initialize the square with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
