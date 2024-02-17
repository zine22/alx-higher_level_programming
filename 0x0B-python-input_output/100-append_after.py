#!/usr/bin/python3
""" Inserts a line of text to a file containing str"""

def append_after(filename="", search_string="", new_string=""):
    """
    function that inserts line of text
    after each line containing a specific string
    Arguments:
        filename: name of file
        search_string: string to be searched
        new_string: string to be placed in next line
    """
    with open(filename, "r", encoding="utf-8") as file:
        rd = file.readlines()

    with open(filename, "w", encoding="utf-8") as file:
        for i in rd:
            file.write(i)
            if search_string in i:
                file.write(new_string)
