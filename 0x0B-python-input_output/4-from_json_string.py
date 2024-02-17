#!/usr/bin/python3
""" From json func """

import json


def from_json_string(my_str):
    """
    function that returns object represented by JSON
    Arguments:
        my_str: json string
    """
    return json.loads(my_str)
