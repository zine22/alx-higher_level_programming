#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        this_page = response.read()

    print("Body response:")
    print("\t- type:", type(this_page))
    print("\t- content:", this_page)
    print("\t- utf8 content:", this_page.decode("utf-8"))
