#!/usr/bin/python3
""" Script that fetches the content of a url """
import urllib.request
import urllib.parse
import sys


def main():
    url = sys.argv[1]
    data = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(data)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(req) as resource:
        print(resource.read().decode('utf-8'))


if __name__ == "__main__":
    main()
