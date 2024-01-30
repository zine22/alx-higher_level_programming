#!/usr/bin/python3
"""
INtegers addition
Module with func to add two int only
If args are not ints error
"""

def add_integer(a, b=98):
    """ a: integer argument
        b: integer argument (default value = 98)
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        if a == float("NaN"):
            raise ValueError("cannot convert float NaN to integer")
        elif (a == float("inf")) or (a == float("-inf")):
            raise OverflowError("cannot convert float infinity to integer")
        else:
            a = int(a)
    if isinstance(b, float):
        if b == float("NaN"):
            raise valueError("vannot convert float NaN to integer")
        elif (a == float("inf")) or (a == float("-inf")):
            raise OverflowError("cannot convert float infinity to integer")
        else:
            b = int(b)
    return a + b
