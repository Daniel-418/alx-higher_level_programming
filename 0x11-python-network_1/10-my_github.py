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
    username = sys.argv[1]
    pat = sys.argv[2]
    url = "https://api.github.com/user"
    auth = HTTPBasicAuth(username, pat)
    req = requests.get(url, auth=auth)
    print(req.json().get("id"))
