#!/usr/bin/python3
""" Save as json file """

import json


def save_to_json_file(my_obj, filename):
    """
    function that writes Object to a text file
    using JSON representation
    Arguments:
        my_obj: Object to be converted
        filename: name of text file
    """
    with open(filename, "w", encoding="utf-8") as file:
        """
        open file
        write to file
        close file
        """
        return file.write(json.dumps(my_obj))
