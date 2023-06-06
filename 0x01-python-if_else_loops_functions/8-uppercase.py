#!/usr/bin/python3

def uppercase(str):
    string = ''
    for character in str:
        if ord(character) >= 97 and ord(character) <= 123:
            string += chr(ord(character) - 32)
        else:
            string += character
    print("{}".format(string))
