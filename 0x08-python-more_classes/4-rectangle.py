#!/usr/bin/python3
"""
Eval is magic
class Rectangle that defines a rectangle
"""


class Rectangle:
    """
    init method of class 'Rectangle'
    """
    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.height = height

    @property
    def width(self):
        """
        method to retrieve self.width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        method to assign integer value to self.width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        method to retrieve self.height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        method to assign integer value to self.height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        returns area if the rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        returns perimeter of the rectangle
        """
        if (self.__width == 0) or (self.__height == 0):
            return 0
        else:
            return (2 * (self.__height + self.__width))

    def __str__(self):
        """
        method to print rectange using '#'
        """
        str_val = ""
        if (self.__height == 0) or (self.__width) == 0:
            return str_val
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    str_val += "#"
                if i != (self.__height - 1):
                    str_val += "\n"
            return str_val

    def __repr__(self):
        return (f"Rectangle({self.__width}, {self.__height})")
