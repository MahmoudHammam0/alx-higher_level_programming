#!/usr/bin/python3
'''POST an email #0 module'''
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    val = {"email": email}
    data = urllib.parse.urlencode(val)
    data = data.encode('ascii')
    with urllib.request.urlopen(url, data) as resp:
        print(resp.read().decode())
