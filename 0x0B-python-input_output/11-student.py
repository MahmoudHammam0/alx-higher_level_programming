#!/usr/bin/python3
'''Student to JSON module'''


class Student:
    '''student class with first, last names and age attributes'''
    def __init__(self, first_name, last_name, age):
        '''initialization'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''retrieves a dictionary representation of a Student'''
        the_dict = {}
        if type(attrs) is list:
            for key, value in self.__dict__.items():
                if key in attrs:
                    the_dict[key] = value
            return the_dict
        return self.__dict__

    def reload_from_json(self, json):
        '''replaces all attributes of the Student instance'''
        self.__dict__ = {}
        for key, value in json.items():
            self.__dict__[key] = value
        return self.__dict__
