#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/izzyofc)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    print("Response status code: {}".format(response.status_code))
    if response.status_code != 200:
        print("Returning 0 due to invalid subreddit or other error")
        return 0
    data = response.json().get("data")
    if data is None:
        print("Returning 0 due to missing data in response")
        return 0
    num_subs = data.get("subscribers", 0)
    print("Number of subscribers: {}".format(num_subs))
    return num_subs
