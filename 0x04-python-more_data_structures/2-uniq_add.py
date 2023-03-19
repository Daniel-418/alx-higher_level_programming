#!/usr/bin/python3

def uniq_add(my_list=[]):
    count = 0;
    uniq_list = set(my_list);

    for i in uniq_list:
        count += i

    return count
