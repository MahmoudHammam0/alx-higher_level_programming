#!/usr/bin/python3
'''Error code #0 module'''
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as resp:
            print(resp.read().decode())
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
