#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        a = None
    else:
        a = sentence[0]
    b = len(sentence)
    tuple_a = (b, a)
    return (tuple_a)
