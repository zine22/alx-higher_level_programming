#!/usr/bin/python3
"""
class 'Square' that defines a square
"""


class Square:
    """
    Defines a square
    Attributes:
        size: size of square
    """

    def __init__(self, size=0):
        """
        init method for class 'Square'
        Args:
            size: size of square
        """
        self.__size = size
        if not (isinstance(self.__size, int)):
            raise TypeError("size must be an integer")
        else:
            if self.__size < 0:
                raise ValueError("size must be >= 0")

    def area(self):
        """
        method for class square
        finds area of the square

        Args:
            size: size of square
        Returns:
            Area of class 'Square'
        """
        return (self.__size ** 2)
