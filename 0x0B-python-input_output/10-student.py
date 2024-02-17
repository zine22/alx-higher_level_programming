#!/usr/bin/python3
""" Class to define a student """

class Student:
    """
    class 'Student' that defines a student
    """
    def __init__(self, first_name, last_name, age):
        """
        init method of class 'Student'
        Arguements:
            first_name: first_name
            last_name = last_name
            age = age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves dictionary representation of a Student instance
        """
        if isinstance(attrs, list):
            dict_val = {}
            for i in attrs:
                if isinstance(i, str) and (i in self.__dict__):
                    dict_val[i] = self.__dict__[i]
            return dict_val
        else:
            return self.__dict__
