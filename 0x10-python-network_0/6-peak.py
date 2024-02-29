#!/usr/bin/python3
'''Find a peak module'''


def find_peak(list_of_integers):
    '''find a peak from a list of unsorted integers'''
    if list_of_integers == []:
        return None
    l = len(list_of_integers)
    if l == 1:
        return list_of_integers[0]
    r_side = find_peak(list_of_integers[:l // 2])
    l_side = find_peak(list_of_integers[l // 2:])
    if l_side > r_side:
        return l_side
    else:
        return r_side
