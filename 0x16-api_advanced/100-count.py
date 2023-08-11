#!/usr/bin/python3
"""
The list of words here
"""


import requests

def count_words(subreddit, word_list, next_page=None):
    # base case: if subreddit is invalid or no posts match
    if subreddit is None:
        return

    # make API request to get hot articles from the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(url, headers={"user-agent": "mozilla/5.0"})

    # check if API request was successful
    if response.status_code == 200:
        data = response.json()
        articles = data['data']['children']

        # dictionary to store word counts
        word_counts = {}

        # iterate over the articles' titles and count the words
        for article in articles:
            title = article['data']['title'].lower()

            # iterate over the word_list and count the occurrences in the title
            for keyword in set(word_list):
                count = title.count(keyword.lower())
                if keyword.lower() not in word_counts:
                    word_counts[keyword.lower()] = count
                else:
                    word_counts[keyword.lower()] += count

        # sort the word counts in descending order of count, and alphabetically if counts are the same
        sorted_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))

        # print the results
        for word, count in sorted_counts:
            print(f"{word}: {count}")

        # recursive call to next page if available
        next_page = data['data']['after']
        if next_page is not None:
            count_words(subreddit, word_list, next_page)
