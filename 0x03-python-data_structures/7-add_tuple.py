#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    fill = (0, )
    if len(tuple_a) < 2:
        for i in range(2):
            if len(tuple_a) == 2:
                break
            tuple_a += fill
    if len(tuple_b) < 2:
        for j in range(2):
            if len(tuple_b) == 2:
                break
            tuple_b += fill
    a = tuple_a[0] + tuple_b[0]
    b = tuple_a[1] + tuple_b[1]
    tuple_c = (a, b)
    return (tuple_c)
