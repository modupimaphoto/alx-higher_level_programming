#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    avg = 0
    result = 0

    for row in my_list:
        avg += row[0] * row[1]
        result += row[0]

    return float(avg / result)
