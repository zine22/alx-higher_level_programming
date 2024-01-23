#!/usr/bin/python3
"""
'Square' class that defines a square
"""


class Square:
    """
    defines a square
    Attributes:
        size
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

    @property
    def size(self):
        """
        method to return size of Square
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        method to assign value to square object
        Args:
            value
        """
        if not (isinstance(self.__size, int)):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        method for class 'Square' to return area of square
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        method for class 'Square' to print '#' in stdout
        """
        if self.__size == 0:
            print("\n", end="")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
