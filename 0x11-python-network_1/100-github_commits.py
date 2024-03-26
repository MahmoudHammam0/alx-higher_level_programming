#!/usr/bin/python3
'''Time for an interview! module'''
import sys
import requests


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    headers = {"Accept": "application/vnd.github+json",
               "X-GitHub-Api-Version": "2022-11-28"
               }
    req = requests.get(url, headers=headers)
    content = req.json()
    try:
        for i in range(10):
            print("{}: {}".format(content[i].get("sha"),
                  content[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
