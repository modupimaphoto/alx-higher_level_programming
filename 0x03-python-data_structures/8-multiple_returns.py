#!/usr/bin/python3

def multiple_returns(sentence):

    if len(sentence) == 0:
        sentence[0] = None

    tuple_s = (sentence)
    first_c = tuple_s[0]

    return (len(tuple_s), first_c)
