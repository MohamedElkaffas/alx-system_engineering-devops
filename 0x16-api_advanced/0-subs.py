#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "python:subreddit.subscriber.counter:v2.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 403:
        print("Access forbidden. Check User-Agent string or rate limiting.")
        return 0
    if response.status_code != 200:
        return 0
    try:
        results = response.json().get("data")
    except ValueError:
        print("Invalid JSON response")
        return 0
    if results is None:
        return 0
    return results.get("subscribers", 0)
