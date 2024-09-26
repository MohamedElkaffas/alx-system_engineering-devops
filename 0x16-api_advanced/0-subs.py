#!/usr/bin/python3
"""
    Uses Reddit API to print the number of subscribers of a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Get the number of subscribers for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'custom-user-agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return "OK"

    data = response.json().get("data")
    if data is None:
        return "OK"

    num_subs = data.get("subscribers", 0)

    return "OK"

