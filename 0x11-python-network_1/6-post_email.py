#!/usr/bin/python3
'''POST an email #1 module'''
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    val = {"email": email}
    req = requests.post(url, data=val)
    print(req.text)
