#!/usr/bin/python3
'''Student to JSON module'''


class Student:
    '''student class with first, last names and age attributes'''
    def __init__(self, first_name, last_name, age):
        '''initialization'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''retrieves a dictionary representation of a Student'''
        return self.__dict__
