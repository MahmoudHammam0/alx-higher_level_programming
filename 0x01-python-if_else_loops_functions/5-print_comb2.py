#!/usr/bin/python3
for a in range(0, 100):
    if a < 10:
        print("0{:d}".format(a), end=", ")
    elif a == 99:
        print("{:d}".format(a))
    else:
        print("{:d}".format(a), end=", ")
