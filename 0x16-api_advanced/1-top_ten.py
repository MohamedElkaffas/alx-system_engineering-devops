mport requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Custom"}
    
    try:
        req = requests.get(url, headers=headers, params={"limit": 10})
        req.raise_for_status()
        
        if req.status_code == 200 and req.text:
            data = req.json()
            posts = data.get("data", {}).get("children", [])
            for post in posts:
                title = post.get("data", {}).get("title")
                print(title)
        else:
            print(None)
    except requests.exceptions.HTTPError:
        print(None)
    except ValueError:
        print(None)

