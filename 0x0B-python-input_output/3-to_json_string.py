#!/usr/bin/python3
'''To JSON string module'''
import json


def to_json_string(my_obj):
    '''return a json representation of an object'''
    return json.dumps(my_obj)
