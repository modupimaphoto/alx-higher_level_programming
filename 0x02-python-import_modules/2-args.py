#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len = len(sys.argv) - 1
    if len == 0:
        print("{} arguments.".format(len))
    elif len == 1:
        print("{} argument:".format(len))
    else:
        print("{} argument:".format(len))
    if len >= 1:
        i = 0
        for arg in sys.argv:
            if i != 0:
                print("{}: {}".format(i, arg))
            i += 1
