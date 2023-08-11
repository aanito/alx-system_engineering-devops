#!/usr/bin/python3
"""
Like that of python here
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-agent": "MyApp/1.0"}

    # send a get request to the reddit api
    response = requests.get(url, headers=headers)

    # check if the subreddit is valid and response is successful
    if response.status_code == 200:
        data = response.json()
        children = data["data"]["children"]

        # append titles of articles to the hot_list
        for child in children:
            hot_list.append(child["data"]["title"])

        # check if there are more pages (pagination)
        if data["data"]["after"]:
            # recursive call to retrieve titles from the next page
            return recurse(subreddit, hot_list, after=data["data"]["after"])
        else:
            return hot_list
    else:
        return None
