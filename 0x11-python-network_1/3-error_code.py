#!/usr/bin/python3
""" Script that fetches the content of a url """
import urllib.request
import urllib.parse
import urllib.error
import sys


def main():
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(req) as resource:
            print(resource.read().decode('utf-8'))

    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    main()
