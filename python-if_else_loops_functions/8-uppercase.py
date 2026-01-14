#!/usr/bin/python3
def uppercase(str):
    text = ""
    for c in str:
        if 97 <= ord(c) <= 122:
            text += chr(ord(c) - 32)
        else:
            text += c
    print("{}".format(text), end="")
    print()
