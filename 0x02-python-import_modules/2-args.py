#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    counter = 0
    arg = len(sys.argv)
    if arg == 2:
        print("1 argument:\n1: {}".format(sys.argv[1]))
    elif arg == 1:
        print("0 arguments.")
    else:
        print("{} arguments:".format(arg - 1))
        for x in range(1, arg):
            counter += 1
            print("{}: {}".format(counter, sys.argv[x]))
