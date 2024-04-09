#!/usr/bin/python3
"""Import modules Here """
import requests


def number_of_subscribers(subreddit):
    """ gets the number of subscribers from a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    header = {
            "User-Agent": "Bakijazzman"
            }
    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
