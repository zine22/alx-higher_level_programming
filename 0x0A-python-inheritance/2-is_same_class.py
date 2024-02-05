#!/usr/bin/python3
"""
Check instamce of a class
"""


def is_same_class(obj, a_class):
    """
    function that returns 'True' if the object is an
        instance of the specified class
    else, 'False'
    """
    return (type(obj) == a_class)
