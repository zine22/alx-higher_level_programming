#!/usr/bin/python3
"""
check for strict inheritance
"""


def inherits_from(obj, a_class):
    """
    function to return 'True'
        if obj inherits from a_class
    else, false
    """
    return ((not type(obj) is a_class) and (issubclass(type(obj), a_class)))
