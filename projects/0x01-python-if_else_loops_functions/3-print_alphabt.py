#!/usr/bin/python3
for i in range(26):
    if (chr(97 + i) == "p" or chr(97 + i) == "e"):
        continue
    print("{}".format(chr(97 + i)), end="")
