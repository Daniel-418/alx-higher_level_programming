#!/usr/bin/python3

def uniq_add(my_list=[]):
    total = 0
    uniq_list = set(my_list)

    for item in uniq_list:
        total += item

    return total
