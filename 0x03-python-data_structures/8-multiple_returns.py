#!/usr/bin/pyton3
def multiple_returns(sentence):
    if sentence == None:
        a = None
    else:
        a = sentence[0]
    b = len(sentence)
    tuple_a = (b, a)
    return (tuple_a)
