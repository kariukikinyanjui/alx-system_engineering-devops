#!/usr/bin/python3
"""
Module: 1-top_ten

This module defines a function to query the Reddit API and print the titles
of the first 10 hot posts listed for a fiven subreddit.

Requirements:
    Prototype: def top_ten(subreddit)
    If not a valid subreddit, print None
    Note: Invalid subreddits may return a redirect to search results.
    Ensure that you are not following redirects.
"""
import requests
import sys


def top_ten(subreddit):
    """Print the titles of the first 10 hot psots for a given subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'CustomUserAgent'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            for post in posts:
                title = post['data']['title']
                print(title)
        else:
            print(None)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        print(None)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        top_ten(subreddit)
