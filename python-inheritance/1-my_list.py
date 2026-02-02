#!/usr/bin/python3
class MyList(list):
    """MyList class that inherits from list"""

    def print_sorted(self):
        """Prints the list sorted in ascending order"""
        print(sorted(self))
