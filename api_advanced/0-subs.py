#!/usr/bin/python3
"""

0-main
"""
import requests


def number_of_subscribers(subreddit):
    """
    Return the number of subscribers for a subreddit.
    If an invalid subreddit is provided, return 0.
    """
    if not subreddit or not isinstance(subreddit, str):
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "python:alx.api_advanced:v1.0 (by /u/shyakafrancis123)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False, timeout=10)
    except requests.RequestException:
        return 0

    if response.status_code != 200:
        return 0

    try:
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    except ValueError:
        return 0
