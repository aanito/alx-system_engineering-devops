
#!/usr/bin/python
"""the reddit advanced api"""

import requests

def top_ten(subreddit):
    # set a custom user-agent to avoid too many requests error
    headers = {"user-agent": "my reddit api client"}

    # make the api request
    url = f"https://www.reddit.com/dev/api/hot.json?limit=10"
    response = requests.get(url, headers=headers, allow_redirects=False)

    # check if the request was successful
    if response.status_code != 200:
        print("None")
        return

    # parse the response to get the titles of the first 10 hot posts
    data = response.json()
    posts = data["data"]["children"]
    for post in posts:
        title = post["data"]["title"]
        print(title)

# example usage
top_ten("python")

