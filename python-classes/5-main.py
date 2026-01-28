#!/usr/bin/python3
Square = __import__("5-square").Square

mysquare = Square(3)
mysquare.my_print()

print("-")

mysquare.size = 10
mysquare.my_print()

print("-")

mysquare.size = 0
mysquare.my_print()

print("-")
