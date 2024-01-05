#!/usr/bin/python3
def magic_string(n_times=[0]):
    n_times[0] = n_times[0] + 1
    return "BestSchool" + (", BestSchool" * (n_times[0] - 1))
