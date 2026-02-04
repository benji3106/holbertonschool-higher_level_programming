#!/usr/bin/python3
"""
This module defines an abstract Shape class and concrete implementations
Circle and Rectangle, along with a function using duck typing.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract class that defines a geometric shape.
    """

    @abstractmethod
    def area(self):
        """
        Returns the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Returns the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Class that defines a Circle, subclass of Shape.
    """

    def __init__(self, radius):
        """
        Initialize the circle with a radius.

        Args:
            radius (int or float): radius of the circle
        """
        self.radius = radius

    def area(self):
        """
        Returns the area of the circle.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Returns the perimeter of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Class that defines a Rectangle, subclass of Shape.
    """

    def __init__(self, width, height):
        """
        Initialize the rectangle with width and height.

        Args:
            width (int or float): width of the rectangle
            height (int or float): height of the rectangle
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of a shape using duck typing.

    Args:
        shape: any object with area() and perimeter() methods
    """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())


if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 3)

    shape_info(circle)
    shape_info(rectangle)
