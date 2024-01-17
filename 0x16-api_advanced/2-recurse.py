#!/usr/bin/python3
"""
A recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit
"""
import requests
import sys


def recurse(subreddit, hot_list=None, after=None):
    """
    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): A list to store the titles of hot articles
        after (str): The 'after' parameter for pagination

    Returns:
        list or None
"""

    if hot_list is None:
        hot_list = []

    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'

    if after:
        url += f'&after={after}'

    headers = {'User-Agent': 'CustomUserAgent'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            for post in posts:
                title = post['data']['title']
                hot_list.append(title)

            after = data['data']['after']

            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None

    except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        result = recurse(subreddit)
        if result is not None:
            print(len(result))
        else:
            print("None")
