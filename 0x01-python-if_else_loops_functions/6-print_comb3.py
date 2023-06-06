#!/usr/bin/python3

for tens in range(0, 10):
    for ones in range(tens + 1, 10):
        if (tens * 10 + ones) != 89:
            print("{}{}".format(tens, ones), end=', ')
        else:
            print("{}{}".format(tens, ones))
