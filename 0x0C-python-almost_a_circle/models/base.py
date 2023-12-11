#!/usr/bin/python3
'''Base class module'''
import json


class Base:
    '''Base class'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''initialization'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''return json representation of list_dictionaries'''
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes the JSON string representation of list_objs to a file'''
        filename = "{}.json".format(cls.__name__)
        if list_objs is None:
            content = "[]"
        else:
            x = []
            for obj in list_objs:
                x.append(obj.to_dictionary())
            content = Base.to_json_string(x)
        with open(filename, mode='w', encoding='UTF8') as my_file:
            my_file.write(content)

    @staticmethod
    def from_json_string(json_string):
        '''returns the list of the JSON string representation'''
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''returns an instance with all attributes already set'''
        if "size" in dictionary:
            dummy = cls(1)
        else:
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''returns a list of instances'''
        filename = "{}.json".format(cls.__name__)
        res = []
        try:
            with open(filename, mode='r', encoding='UTF8') as my_file:
                content = my_file.read()
        except FileNotFoundError:
            return []
        x = Base.from_json_string(content)
        for ins in x:
            res.append(cls.create(**ins))
        return res
