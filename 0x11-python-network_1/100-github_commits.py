#!/usr/bin/python3
"""
Script that list 10 commits
of a specified repository
"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
            sys.argv[2], sys.argv[1])
    r = requests.get(url)

    for json in r.json()[:10]:
        print('{}: {}'.format(json.get('sha'), json.get('commit').get(
              'author').get('name')))
