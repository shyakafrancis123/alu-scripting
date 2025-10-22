#!/usr/bin/python3
"""
Contains the function top_ten that queries the Reddit API
and prints the titles of the first 10 hot posts for a subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first
    10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "python:reddit-api-client:v1.0 (by /u/yourusername)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            for post in data.get("data", {}).get("children", []):
                print(post["data"]["title"])
        else:
            print(None)
    except requests.RequestException:
        print(None)
