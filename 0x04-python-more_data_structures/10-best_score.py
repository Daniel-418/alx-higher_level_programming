#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary == None:
        return None

    maximum = list(a_dictionary.keys())[0]
    for key in a_dictionary.keys():
        if a_dictionary[key] > a_dictionary[maximum]:
            maximum = key

    return maximum
