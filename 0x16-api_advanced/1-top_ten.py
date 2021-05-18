#!/usr/bin/python3
"""function request a api"""
import requests
from sys import argv


def top_ten(subreddit):
    """function request a api with top 10 topics"""
    try:
        url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(argv[1])
        user_agent = "coco"
        headers = {'User-Agent': user_agent}
        response = requests.get(url, headers=headers)
        json_request = response.json()
        data = json_request.get('data')
        if data is not None:
            posts = data.get('children')
            for i in posts:
                print(i.get('data').get('title'))
        else:
            print(None)
        return (number_subscribers)
    except Exception as err:
        return (None)
