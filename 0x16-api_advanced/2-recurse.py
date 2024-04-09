#!/usr/bin/python3
"""Import Modules Here """
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """retrns a list containing the titles of all hot articles
    for a given subreddit"""
    global after
    url = "https://www.reddit.com/r/{}/hot.json.".format(subreddit)
    header = {"User-Agent": "Bakijazzman"}
    param = {'after': after}
    response = requests.get(url, headers=header, params=param,
                            allow_redirects=False)
    if response.status_code == 200:
        after_data = response.get("data").get("after")
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        all_titles = response.json().get("data").get("children")
        for title_ in all_titles:
            hot__list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)
