#!/usr/bin/python3

def pow(a, b):
    if a == 0:
        return 0
    power = 1
    for i in range(abs(b)):
        power = power * a
    if b >= 0:
        return power
    else:
        return 1 / power
