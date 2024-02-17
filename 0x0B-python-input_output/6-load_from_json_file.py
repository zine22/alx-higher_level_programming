#!/usr/bin/python3
""" Load as json file """

import json


def load_from_json_file(filename):
    """
    function that creates Object from a JSON file
    Arguments:
        filename: name of file
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.loads(file.read())
