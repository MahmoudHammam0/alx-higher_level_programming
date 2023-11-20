#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        res = fct(*args)
        return (res)
    except (IndexError, ZeroDivisionError) as Exception:
        print("Exception:", Exception, file=sys.stderr)
        return (None)
