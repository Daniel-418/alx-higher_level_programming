#!/usr/bin/python3
""" Script that fetches the content of a url """
import requests


def main():
    response = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t - type: {}".format(type(response).__name__))
    print("\t - content: {}".format(response.text()))


if __name__ == "__main__":
    main()
