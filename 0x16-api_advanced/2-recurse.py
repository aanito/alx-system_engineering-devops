#!/usr/bin/python3
"""
Like that of python here
"""

import requests

def recurse(subreddit, hot_list=[]):
    base_url = 'https://www.reddit.com/dev/api/hot.json'.format(subreddit)

    # Send a GET request to the Reddit API
    response = requests.get(base_url, headers={'User-agent': 'Mozilla/5.0'})

    # Check if the subreddit is valid
    if response.status_code == 404:
        return None

    # Retrieve the JSON response data
    data = response.json()
    children = data['data']['children']

    # Iterate through the children (articles) and add their titles to the hot_list
    for child in children:
        hot_list.append(child['data']['title'])

    # Check if there are more pages to retrieve
    if data['data']['after'] is not None:
        # Recursive call to fetch the next page of results
        recurse(subreddit, hot_list=hot_list)

    return hot_list
