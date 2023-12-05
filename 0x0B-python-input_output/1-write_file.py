#!/usr/bin/python3
'''Write to a file module'''


def write_file(filename="", text=""):
    '''overwrite contents of a file'''
    with open(filename, mode='w', encoding='UTF8') as my_file:
        num_of_char = my_file.write(text)
    return num_of_char
