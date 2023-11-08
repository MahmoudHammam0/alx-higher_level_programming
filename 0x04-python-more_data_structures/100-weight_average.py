#!/usr/bin/python3
def weight_average(my_list=[]):
    if (len(my_list) == 0):
        return 0
    total = 0
    div = 0
    for the_tuple in my_list:
        x, y = the_tuple
        total += (x * y)
        div += y
    res = total / div
    return (res)
