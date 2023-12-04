#!/usr/bin/python3
'''Can I? module'''


def add_attribute(obj, att_name, att_value):
    '''set a new attribute to object if possible'''
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att_name, att_value)
