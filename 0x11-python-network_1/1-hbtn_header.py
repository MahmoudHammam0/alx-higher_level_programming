#!/usr/bin/python3
'''Response header value #0 module'''
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as resp:
        print(resp.info().get("X-Request-Id"))
