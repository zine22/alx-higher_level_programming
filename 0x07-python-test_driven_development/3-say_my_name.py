#!/usr/bin/python3
"""
Say my name
Module comtaining function that prints name
"""


def say_my_name(first_name, last_name=""):
    """
    function that prints name
    Arguments:
        first_name: first argument
        last_name: second argument
    """
    if not isinstance(first_name, str):
        """
        check if first_name is of type <class 'str'>
        """
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        """
        check is last_name is of type <class 'str'>
        """
        raise TypeError("last_name must be a string")
    else:
        """
        prints string to stdout
        """
        print("My name is {:s} {:s}".format(first_name, last_name))
