#!/usr/bin/python3
""" POST email to given URL and prints response.
"""


import urllib.parse
import urllib.request
import sys


if __name__ == '__main__':
    data = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(data).encode('ascii')
    request = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(request) as response:
        html = response.read()
        print(html.decode('utf-8'))
