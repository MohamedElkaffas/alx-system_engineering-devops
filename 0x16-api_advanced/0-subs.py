
n that returns the number of subscribers for a given subreddit"""
import requests

def number_of_subscribers(subreddit):
    """Gets number of subscribers
       Args:
           subreddit (str): name of subreddit
       Returns:
           number of subscribers if valid, 0 otherwise
    """
    base_url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'custom-user-agent'}
    
    try:
        # Fetch the subreddit info
        response = requests.get(base_url, headers=headers, allow_redirects=False)
        
        # If the response code is not 200, it's either not found or another issue
        if response.status_code != 200:
            return 0
        
        # Load the JSON response
        data = response.json()
        
        # Extract the number of subscribers
        return data.get('data', {}).get('subscribers', 0)
    
    except (requests.RequestException, ValueError, KeyError):
        # Return 0 in case of any network error or invalid JSON structure
        return 0

