#!/usr/bin/python3
""" Script that fetches the content of a url """
import requests
import sys


def main():
    response = requests.get(sys.argv[1])
    print("{}".format(response.headers.get('X-Request-Id')))


if __name__ == "__main__":
    main()
