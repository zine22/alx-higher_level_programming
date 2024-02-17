#!/usr/bin/python3
""" Func to return the dictionary description """

def class_to_json(obj):
    """
    returns dictionary description of obj
    Arguments:
        obj
    """
    return obj.__dict__
