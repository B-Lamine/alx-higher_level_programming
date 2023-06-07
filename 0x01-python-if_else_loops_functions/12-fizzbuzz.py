#!/usr/bin/python3

def fizzbuzz():
    fizz = 'Fizz'
    buzz = 'Buzz'
    for i in range(1, 101):
        if (i % 3 == 0) or (i % 5 == 0):
            if i % 3 == 0:
                print(fizz, end='')
            if i % 5 == 0:
                print(buzz, end='')
        else:
            print(i, end='')
        print(' ', end='')
    return
