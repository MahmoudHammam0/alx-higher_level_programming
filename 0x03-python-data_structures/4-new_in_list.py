#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    length = len(my_list) - 1
    if (idx < 0) or (idx > length):
        return (new_list)
    new_list[idx] = element
    return (new_list)
