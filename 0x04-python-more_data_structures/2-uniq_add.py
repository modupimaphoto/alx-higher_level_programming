#!/usr/bin/python3

def uniq_add(my_list=[]):
    my_set = set(my_list)
    my_list = list(my_set)
    result = 0

    for i in my_list:
        result += i
    return result
