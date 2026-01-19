#!/usr/bin/python3
def no_c(my_string):
    chars = list(my_string)

    while 'c' in chars:
        chars.remove('c')

    while 'C' in chars:
        chars.remove('C')

    return "".join(chars)
