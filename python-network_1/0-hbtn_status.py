#!/usr/bin/python3
"""Script that fetches https://alu-intranet.hbtn.io/status using urllib"""
import urllib.request


with urllib.request.urlopen('https://alu-intranet.hbtn.io/status') as response:
    body = response.read()
    print("Body response:")
    print("	- type: {}".format(type(body)))
    print("	- content: {}".format(body))
    print("	- utf8 content: {}".format(body.decode('utf-8')))
