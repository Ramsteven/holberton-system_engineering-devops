#!/usr/bin/python3
"""Request api return hotlist"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """list containing the titles"""
    api = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={'User-agent': 'coco'}, params={'after': after})

    if not api:
        return None
    else:
        rr = api.json().get('data').get('children')
        for json_dict in rr:
            hot_list.append(json_dict.get('data').get('title'))
        if api.json().get('data').get('after') is not None:
            after = api.json().get('data').get('after')
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
