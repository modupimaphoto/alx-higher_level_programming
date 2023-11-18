#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    list_cpy = my_list[:]
    length = len(list_cpy) - 1

    if idx < 0 or idx > length:
        return list_cpy
    else:
        list_cpy[idx] = element
        return list_cpy
