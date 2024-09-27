#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    username = 'Bubbly-Mud1048'
    password = 'tempa7ad@3'
    user_pass_dict = {'user': username, 'passwd': password, 'api_type': 'json'}
    headers = {'user-agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/Bubbly-Mud1048)'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    
    client = requests.session()
    client.headers = headers
    client.post('https://www.reddit.com/api/login', data=user_pass_dict)
    
    response = client.get(url, allow_redirects=False)
    if response.status_code != 404:
        return response.json().get("data", {}).get("subscribers", 0)
    else:
        return 0
