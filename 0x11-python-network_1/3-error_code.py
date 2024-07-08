#!/usr/bin/python3
"""
a Python script that takes in a URL,
sends a request to the URL and
displays the body of the response (decoded in utf-8)
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    """
    Just checking for something here

    with urllib.request.Request(url) as req:
        try:
            urllib.request.urlopen(req)

        except urllib.error.HTTPError as e:
            print("Error code:", e.code)
    """

    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as response:
            response_body = response.read().decode("utf-8")
            print(response_body)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
