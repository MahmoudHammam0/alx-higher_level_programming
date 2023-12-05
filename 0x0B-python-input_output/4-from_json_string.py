#!/usr/bin/python3
'''From JSON string to Object module'''
import json


def from_json_string(my_str):
    '''return an object from json string'''
    return json.loads(my_str)
