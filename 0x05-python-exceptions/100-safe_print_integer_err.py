#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError) as Exception:
        print("Exception:", Exception, file=sys.stderr)
        return (False)
