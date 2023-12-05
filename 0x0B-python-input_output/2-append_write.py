#!/usr/bin/python3
'''Append to a file module'''


def append_write(filename="", text=""):
    '''appends text to file'''
    with open(filename, mode='a', encoding='UTF8') as my_file:
        num_of_char = my_file.write(text)
    return num_of_char
