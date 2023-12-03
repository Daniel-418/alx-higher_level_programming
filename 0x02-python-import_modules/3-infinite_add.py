#!/usr/bin/python3
"""module that adds all the arguments"""

from sys import argv


def main():
    total = 0
    args_len = len(argv)

    if args_len > 1:
        for argument in argv[1:]:
            value = int(argument)
            total += value

    print("{}".format(total))


if __name__ == "__main__":
    main()
