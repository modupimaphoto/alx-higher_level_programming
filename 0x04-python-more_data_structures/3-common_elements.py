#!/usr/bin/python3

def common_elements(set_1, set_2):
    list_1 = list(set_1)
    list_2 = list(set_2)
    common_elements = []

    for i in list_1:
        for j in list_2:
            if i == j:
                common_elements.append(i)
    return common_elements
