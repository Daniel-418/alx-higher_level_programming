#!/usr/bin/python3

def islower(c):
    """Checks if a character is lowercase"""
    ascii_value = ord(c)
    if ascii_value > 96 and ascii_value < 123:
        return True
    else:
        return False
