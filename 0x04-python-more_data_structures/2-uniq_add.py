#!/usr/bin/python3
def uniq_add(my_list=[]):
    temp = []
    result = 0
    for i in my_list:
        if i in temp:
            continue
        else:
            temp.append(i)
            result += i
    return result
