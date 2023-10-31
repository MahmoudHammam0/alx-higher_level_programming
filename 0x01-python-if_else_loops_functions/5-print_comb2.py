#!/usr/bin/python3
for a in range(0, 100):
    if a < 10:
        x = "0" + str(a)
    else:
        x = str(a)
    if a == 99:
        print("{:d}".format(a))
        break
    print("{:s}".format(x), end=", ")
