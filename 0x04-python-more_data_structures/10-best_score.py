#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        new_list = []
        for i, j in a_dictionary.items():
            new_list.append(j)
            new_list.sort()
        for x, y in a_dictionary.items():
            if y == new_list[-1]:
                return (x)
    else:
        return (None)
