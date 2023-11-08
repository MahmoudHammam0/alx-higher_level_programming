#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for a_key, a_value in a_dictionary.copy().items():
        if value == a_value:
            del (a_dictionary[a_key])
    return (a_dictionary)
