#!/usr/bin/python3
"""
    Uses reddit API to print # of subscribers of a subreddit
"""
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """Get the numbers of subscribers by subreddit given"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return False
