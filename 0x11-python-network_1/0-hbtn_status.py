#!/usr/bin/python3
""" Script that fetches the content of a url """
import urllib.request


def main():
    with urllib.request.urlopen(
            "https://alx-intranet.hbtn.io/status") as resource:
        content = resource.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))


if __name__ == "__main__":
    main()
