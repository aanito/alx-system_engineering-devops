#!/usr/bin/python3
"""
The list of words here
"""



import requests

def count_words(subreddit, word_list, after=None, count={}):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
    params = {'after': after} if after else {}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        print("Invalid subreddit or error occurred")
        return

    data = response.json()
    articles = data['data']['children']

    for article in articles:
        title = article['data']['title'].lower()
        for word in word_list:
            word = word.lower()
            if word in title:
                count[word] = count.get(word, 0) + title.count(word)

    after = data['data']['after']
    if after:
        count_words(subreddit, word_list, after, count)
    else:
        sorted_count = dict(sorted(count.items(), key=lambda item: (-item[1], item[0])))
        for word, cnt in sorted_count.items():
            print(f"{word}: {cnt}")


# Example usage
#count_words("python", ["python", "java", "javascript"])

