#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            upper_c = ord(c) - 32
        else:
            upper_c = ord(c)
        print("{:c}".format(upper_c), end="")
    print()
