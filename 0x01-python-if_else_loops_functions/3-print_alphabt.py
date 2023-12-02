#!/usr/bin/python3
for i in range(26):
    letter = chr(97 + i)
    if (letter == 'q' or letter == 'e'):
        continue
    print(f"{}".format(letter), end="")
