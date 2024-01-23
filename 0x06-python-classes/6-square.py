#!/usr/bin/python3
"""
'Square' class that defines a square
"""


class Square:
    """
    defines a square
    Attributes:
        size: size of square
        position: position of square object on cartesian plane
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        init method for class 'Square'
        Args:
            size: size of square
            position: position of square on cartesian plane
        """
        self.size = size
        self.position = position

        """
        if not (isinstance(self.__size, int)):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        """

        """
        if ((not isinstance(self.__position[0], int)) or
                (not isinstance(self.__position[1], int))):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (not isinstance(self.__position, tuple) or
                (self.__position[0] < 0) or (self.__position[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(self.__position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        """

    @property
    def size(self):
        """
        method of class Square
        Returns:
            size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        method to assign value to size
        Args:
            value: value for size
        """
        if not (isinstance(value, int)):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        method to return a tuple of two positive integers
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        method to assign value to position
        Args:
            value: tuple value for position
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif ((not isinstance(value[0], int)) or
                (not isinstance(value[1], int))):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        method to return area of square

        Returns:
            area of Square object
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        method to print '#' to form square
        """
        if (self.__size == 0):
            print("")
            return
        for i in range(self.__position[1]):
            print("")
        for j in range(self.__size):
            for x in range(self.__position[0]):
                print(" ", end="")
            for y in range(self.__size):
                print("#", end="")
            print("")
