#!/usr/bin/python3
"""
A Python script that takes your GitHub credentials
(username and password) and uses the GitHub API
to display your id
"""
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(
            owner, repo)
    req = requests.get(url)
    commits = req.json()

    try:
        for num in range(10):
            print("{}: {}".format(
                commits[num].get('sha'), commits[num].get(
                    'commit').get('author').get('name')))
    except IndexError:
        pass
