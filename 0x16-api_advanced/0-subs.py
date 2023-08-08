#!/usr/bin/python
"""The reddit advanced api"""

import requests

def number_of_subscribers(subreddit):
    # Set a custom user-agent to avoid too many requests error
    headers = {"User-Agent": "My Reddit API Client"}

    # Make the API request
    url = f"https://www.reddit.com/dev/api/"
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code != 200:
        # Invalid subreddit or some other error occurred
        return 0

    # Parse the response to get the number of subscribers
    data = response.json()
    subscribers = data["data"]["subscribers"]

    return subscribers

