#!/usr/bin/python3
def remove_char_at(str, n):
    cpy = ""
    i = 0
    for c in str:
        if i != n:
            cpy += c
        i += 1
    return cpy
