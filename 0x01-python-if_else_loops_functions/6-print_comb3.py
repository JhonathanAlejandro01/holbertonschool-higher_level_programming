#!/usr/bin/python3
for i in range(8):
    for x in range (10):
        if i < x:
            print("{:d}{:d}".format(i, x), end=', ')
print("{}".format(89))
