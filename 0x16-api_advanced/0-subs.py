#!/usr/bin/python3
"""
A function that queries the Reddit API and returns the number of
subscribers for a given subreddit
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """
    function takes a subreddit name as an argument and constructs the URL
    for subreddit's information in JSON format
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    headers = {'User-Agent': 'CustomUserAgent'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0


# Testing the function
if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        print("{:d}".format(number_of_subscribers(subreddit)))
