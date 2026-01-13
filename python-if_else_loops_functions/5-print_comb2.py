#!/usr/bin/python3

for loop in range(100):
    print("{}".format(loop), end=', ') if loop < 99 else print("{}".format(loop), end='')
