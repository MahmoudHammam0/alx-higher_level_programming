#!/usr/bin/python3
for a in range(0, 9):
    for b in range(a + 1, 10):
        print("{:d}{:d}".format(a, b), end='')
        if a == 8 and b == 9:
            print("\n", end='')
            break
        print(", ", end='')
