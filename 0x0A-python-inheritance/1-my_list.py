#!/usr/bin/python3
"""
contains MyList class
"""


class MyList(list):
    """
    Inherits from class 'list'
    """
    def __init__(self):
        """
        init method for class 'MyList'
        """
        pass

    def print_sorted(self):
        """
        method to print a sorted list
        in ascending order
        """
        print(sorted(self))
