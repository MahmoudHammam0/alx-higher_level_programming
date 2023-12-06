#!/usr/bin/python3
'''Search and update module'''


def append_after(filename="", search_string="", new_string=""):
    '''inserts line to a file, after each line containing a specific string'''
    with open(filename, mode='r+', encoding='UTF8') as my_file:
        lines = my_file.readlines()
        my_file.seek(0)
        for line in lines:
            if search_string in line:
                my_file.write(line)
                my_file.write(new_string)
            else:
                my_file.write(line)
