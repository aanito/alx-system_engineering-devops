#!/usr/bin/python
"""The reddit advanced api"""

import json
import requests
import sys

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers for a given subreddit."""
    headers = {'User-Agent': 'Custom User-Agent/1.0'}
    url = f'https://www.reddit.com/dev/api/{subreddit}/about.json'
    
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        if 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            return 0
    except:
        return 0

