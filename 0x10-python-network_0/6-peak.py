#!/usr/bin/python3
'''Find a peak module'''


def find_peak(list_of_integers):
    '''find a peak from a list of unsorted integers'''
    if list_of_integers == []:
        return None
    i = 0
    j = len(list_of_integers) - 1
    while i < j:
        x = (i + j) // 2
        if list_of_integers[x] < list_of_integers[x + 1]:
            i = x + 1
        else:
            j = x
    return list_of_integers[i]
