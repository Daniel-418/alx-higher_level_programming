#!/usr/bin/python3
"""module that prints the arguments passed to it"""
from sys import argv


def main():
    """
    main - prints all the arguments passed to the program

    Return: void
    """
    counter = 1
    args_len = len(argv)

    print("{} {}{}".format(
                args_len - 1,
                "argument" if args_len == 2 else "arguments",
                "." if args_len == 1 else ":"))
    if args_len > 1:
        for i in range(1, args_len):
            print("{}: {}".format(counter, argv[i]))
            counter += 1


if __name__ == "__main__":
    main()
