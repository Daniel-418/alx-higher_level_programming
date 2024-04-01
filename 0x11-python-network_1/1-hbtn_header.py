#!/usr/bin/python3
""" Script that fetches the content of a url """
import urllib.request
import sys


def main():
    url = sys.argv[1]
    with urllib.request.urlopen(url) as resource:
        print(resource.info()['X-Request-Id'])


if __name__ == "__main__":
    main()
