#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    list_1 = list(set_1)
    list_2 = list(set_2)
    list_1 += list_2
    
    return set(list_1)
