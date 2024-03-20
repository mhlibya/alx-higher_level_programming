#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for i in my_list:
        if i == search:
            n = replace
        else:
            n = i
        new_list.append(n)
    return new_list
