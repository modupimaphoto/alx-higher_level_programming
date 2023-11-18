#!/usr/bin/python3

def multiple_returns(sentence):

    if sentence == "":
        return (0, None)

    tuple_s = (sentence)
    first_c = sentence[0]

    return (len(tuple_s), first_c)
