#!/usr/bin/python3
def uppercase(str):
    for a in str:
        n = ord(a)
        if ord(a) >= 97 and ord(a) <= 122:
            n = ord(a) - 32
        print("{:c}".format(n), end='')
    print()
