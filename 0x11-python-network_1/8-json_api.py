#!/usr/bin/python3
'''Search API module'''
import sys
import requests


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    letter = ""
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    val = {"q": letter}
    req = requests.post(url, data=val)
    try:
        content = req.json()
        if content == {}:
            print("No result")
        else:
            print("[{}] {}".format(content.get("id"), content.get("name")))
    except requests.exceptions.JSONDecodeError as e:
        print("Not a valid JSON")
