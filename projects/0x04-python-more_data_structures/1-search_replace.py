#!/usr/bin/python3

def search_replace(my_list, search, replace):
    def replace_in_list(x):
        if x == search:
            return replace
        else:
            return x

    return [replace_in_list(x) for x in my_list]
