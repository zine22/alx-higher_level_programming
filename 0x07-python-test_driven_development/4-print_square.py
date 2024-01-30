#!/usr/bin/python3
"""
Print square
Module with function to print a square with the character '#'
"""


def print_square(size):
    """
    prints square with the "#" character
    Arguments:
        size: size of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
