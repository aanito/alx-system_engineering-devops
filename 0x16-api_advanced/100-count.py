#!/usr/bin/python3

import requests

def count_words(subreddit, word_list, count_dict=None):
    if count_dict is None:
        count_dict = {}

    url = f"https://www.reddit.com/dev/api//{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        for post in data["data"]["children"]:
            title = post["data"]["title"]
            title_words = title.lower().split()

            for word in word_list:
                word_lowercase = word.lower()

                if word_lowercase in title_words:
                    if word_lowercase in count_dict:
                        count_dict[word_lowercase] += title_words.count(word_lowercase)
                    else:
                        count_dict[word_lowercase] = title_words.count(word_lowercase)

        if data["data"]["after"] is not None:
            return count_words(subreddit, word_list, count_dict)
        else:
            sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))

            for word, count in sorted_counts:
                print(f"{word}: {count}")

    elif response.status_code == 404:
        print("Invalid subreddit")
    else:
        print("An error occurred")

count_words("python", ["python", "java", "JavaScript"])
