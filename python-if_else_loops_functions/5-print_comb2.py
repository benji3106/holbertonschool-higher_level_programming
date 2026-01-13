#!/usr/bin/python3

for loop in range(100):
    if loop < 99:
        print("{:02d}".format(loop), end=', ')
    else:
        print("{:02d}".format(loop), end='\n')
