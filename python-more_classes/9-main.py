#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

mysquare = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(
    mysquare.area(), mysquare.perimeter()
))
print(mysquare)
