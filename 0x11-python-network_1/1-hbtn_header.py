#!/usr/bin/python3
""" Get X-Request-Id variable from URL.
"""


import urllib.request
import sys


if __name__ == '__main__':
    request = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(request) as response:
        print(response.getheader('X-Request-Id'))
