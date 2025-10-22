#!/usr/bin/python3
"""
1-main
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts of a subreddit.
    If the subreddit is invalid, prints None.
    """
    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "python:alx.api_advanced:v1.0 (by /u/shyakafrancis123)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False, timeout=10)
    except requests.RequestException:
        print(None)
        return

    if response.status_code != 200:
        print(None)
        return

    try:
        posts = response.json().get("data", {}).get("children", [])
    except ValueError:
        print(None)
        return

    if not posts:
        print(None)
        return

    for post in posts:
        print(post.get("data", {}).get("title"))
