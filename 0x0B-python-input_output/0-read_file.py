#!/usr/bin/python3
'''Read file module'''


def read_file(filename=""):
    '''reads a text file and print to stdout'''
    with open(filename, encoding="UTF8") as my_file:
        print(my_file.read(), end='')
