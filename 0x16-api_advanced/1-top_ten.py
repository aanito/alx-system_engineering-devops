#!/usr/bin/python3
"""
The reddit API requst for the top hot posts of the subreddit 
"""

import requests


def top_ten(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'MyApp/1.0'}
    
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        
        if posts:
            for post in posts:
                print(post['data']['title'])
        else:
            print("None.")
    else:
        if response.status_code == 302:
            print("None")
        else:
            print("None")
