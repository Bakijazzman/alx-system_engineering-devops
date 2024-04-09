#!/usr/bin/python3
"""Import Modules Here """
import requests


def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts for a given
    subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    param = {"limit": 10}
    header = {"User-Agent": "Bakijazzman"}
    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code == 404:
        print("None")
    results = response.json().get("data")
    for child in results.get("children"):
        print(child.get("data").get("title"))
