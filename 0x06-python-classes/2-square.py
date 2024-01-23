#!/usr/bin/python3
"""
class 'Square' that defines a square
"""


class Square:
    """
    Defines a square
    Attributes:
        size: size of the square
    """

    def __init__(self, size=0):
        """
        method for class 'Square'
        Args:
            size
        """
        self.__size = size

        if not (isinstance(self.__size, int)):
            raise TypeError("size must be an integer")
        else:
            if self.__size < 0:
                raise ValueError("size must be >= 0")
