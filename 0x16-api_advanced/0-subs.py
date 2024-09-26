#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/your_username)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    print(f"Response status code: {response.status_code}")  # Debugging line
    if response.status_code != 200:
        print("Returning 0 due to invalid subreddit or other error")  # Debugging line
        return 0
    data = response.json().get("data")
    if data is None:
        print("Returning 0 due to missing data in response")  # Debugging line
        return 0
    num_subs = data.get("subscribers", 0)
    print(f"Number of subscribers: {num_subs}")  # Debugging line
    return num_subs
