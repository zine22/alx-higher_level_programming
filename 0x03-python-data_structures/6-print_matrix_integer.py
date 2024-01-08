#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        if len(x) == 0:
            print()
        for i in range(len(x)):
            print("{:}".format(x[i])
