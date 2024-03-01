#!/usr/bin/python3
'''My GitHub! module'''
import sys
import requests


if __name__ == "__main__":
    name = sys.argv[1]
    passwd = sys.argv[2]
    url = 'https://api.github.com/users/{}'.format(name)
    headers = {"Accept": "application/vnd.github+json",
               "Authorization": "Bearer {}".format(passwd),
               "X-GitHub-Api-Version": "2022-11-28"
               }
    req = requests.get(url, headers=headers)
    print(req.json().get("id"))
