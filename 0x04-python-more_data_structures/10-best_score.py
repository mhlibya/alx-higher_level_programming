#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    maximum = max(a_dictionary.values())
    for key in a_dictionary:
        if a_dictionary.get(key) == maximum:
            return key
