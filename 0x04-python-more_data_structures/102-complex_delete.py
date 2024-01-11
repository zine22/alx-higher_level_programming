#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    ky = list(a_dictionary.keys())

    for i in ky:
        if value == a_dictionary[i]:
            del a_dictionary[i]
    return a_dictionary
