#!/usr/bin/python3
def islower(c):
    ascii_value = ord(c)
    if ascii_value < 97 or ascii_value > 122:
        return False
    else:
        return True
