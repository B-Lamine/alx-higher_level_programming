#!/usr/bin/python3
""" Get type and content from URL.
"""


import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status')\
            as response:
        html = response.read()
    print("Body response:")
    print('\t- type:', type(html))
    print('\t- content:', html)
    print('\t- utf8 content:', html.decode('utf-8'))
