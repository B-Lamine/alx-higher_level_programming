#!/usr/bin/python3
""" Get X-Request-Id variable from URL.
"""


import requests
import sys


if __name__ == '__main__':
    response = requests.get(sys.argv[1])
    print(response.headers.get('X-Request-Id'))
