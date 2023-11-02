#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    arg = len(sys.argv)
    for x in range(1, arg):
        num = int(sys.argv[x])
        sum += num
    print("{}".format(sum))
