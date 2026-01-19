#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for i, n in enumerate(line):
            if i != len(line) - 1:
                print("{:d} ".format(n), end="")
            else:
                print("{:d}".format(n), end="")
        print()
