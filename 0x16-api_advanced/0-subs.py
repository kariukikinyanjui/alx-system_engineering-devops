#!/usr/bin/python3
import requests
import sys
"""
A function that queries the Reddit API and returns the number of
subscribers for a given subreddit
"""


def number_of_subscribers(subreddit):
    """
    function takes a subreddit name as an argument and constructs the URL
    for subreddit's information in JSON format
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    headers = {'User-Agent': 'CustomUserAgent'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            return 0

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        print("{:d}".format(number_of_subscribers(subreddit)))
