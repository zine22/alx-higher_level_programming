#!/usr/bin/python3
""" Define a student with a list """

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

    def to_json(self):
        """
        retrieves dictionary representation of a Student instance
        """
        return self.__dict__
