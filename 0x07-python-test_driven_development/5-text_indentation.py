#!/usr/bin/python3
"""
Text indentation
Module that contains function to output text
"""


def text_indentation(text):
    """
    function to output test
    Arguments:
        text: text to be indented and printed
    """
    if not isinstance(text, str):
        """
        checks if text is of type <class 'int'>
        if False, TypeError is raised
        """
        raise TypeError("text must be a string")
    else:
        str_val = ""
        val = ""
        for i in range(len(text)):
            if (text[i] not in [".", "?", ":"]):
                if (text[i]) == " ":
                    if (text[i - 1] in [".", "?", ":"]):
                        continue
                print("{}".format(text[i]), end="")
            else:
                print("{}".format(text[i]))
                print()
