#!/usr/bin/python3
'''Find a peak module'''


def find_peak(list_of_integers):
    '''find a peak from a list of unsorted integers'''
    if list_of_integers == []:
        return None
    return (max(list_of_integers))
