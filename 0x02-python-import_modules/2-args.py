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

    print("{} arguments.".format(args_len - 1))
    if args_len > 1:
        for i in range(1, args_len):
            print("{}: {}".format(counter, argv[i]))
            counter += 1


if __name__ == "__main__":
    main()
