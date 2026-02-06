#!/usr/bin/python3
"""
This module defines SwimMixin and FlyMixin classes and a Dragon class
that demonstrates mixin-based inheritance.
"""


class SwimMixin:
    """
    Mixin that provides swimming behavior.
    """

    def swim(self):
        """
        Print swimming behavior.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin that provides flying behavior.
    """

    def fly(self):
        """
        Print flying behavior.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class that can both swim and fly.
    """

    def roar(self):
        """
        Print dragon roar.
        """
        print("The dragon roars!")
