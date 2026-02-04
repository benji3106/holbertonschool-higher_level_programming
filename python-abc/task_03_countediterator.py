#!/usr/bin/python3
"""
This module defines a CountedIterator class that wraps an iterator
and counts how many items have been iterated over.
"""


class CountedIterator:
    """
    Iterator that counts the number of items fetched.
    """

    def __init__(self, iterable):
        """
        Initialize the iterator and the counter.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """
        Return the next item and increment the counter.
        """
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """
        Return the number of items iterated over.
        """
        return self.count
