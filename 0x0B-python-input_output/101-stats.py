#!/usr/bin/python3
'''Log parsing module'''


def status_printed(size, status_codes):
    '''print each 10 lines'''
    print("File size: {}".format(size))
    for sig in sorted(status_codes):
        print("{}: {}".format(sig, status_codes[sig]))


if __name__ == "__main__":
    import sys

    num = 0
    size = 0
    status = {}
    codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    try:
        for line in sys.stdin:
            if num == 10:
                status_printed(size, status)
                num = 1
            else:
                num += 1
            line = line.split()
            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass
            try:
                if line[-2] in codes:
                    if status.get(line[-2], -1) == -1:
                        status[line[-2]] = 1
                    else:
                        status[line[-2]] += 1
            except IndexError:
                pass
        status_printed(size, status)
    except KeyboardInterrupt:
        status_printed(size, status)
        raise
