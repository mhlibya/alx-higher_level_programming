#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    my_dict = {}
    for key in a_dictionary:
        value = a_dictionary.get(key) * 2
        my_dict.update({key: value})
    return my_dict
