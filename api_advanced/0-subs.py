#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers
for a given subreddit.

Prototype: def number_of_subscribers(subreddit)

If the subreddit is invalid or an error occurs, returns 0.

Notes:
- No authentication required.
- Do not follow redirects for invalid subreddits (allow_redirects=False).
- Use a custom User-Agent to avoid 429 Too Many Requests.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Return the number of subscribers for a subreddit.

    subreddit (str): name of the subreddit (e.g. "python").

    Returns:
        int: total subscribers, or 0 if subreddit is invalid or on error.
    """
    if not subreddit or not isinstance(subreddit, str):
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "python:0-subs:v1.0 (by /u/shyakafrancis123)"}

    try:
        resp = requests.get(url, headers=headers, allow_redirects=False, timeout=10)
    except requests.RequestException:
        return 0

    if resp.status_code != 200:
        return 0

    try:
        data = resp.json()
    except ValueError:
        return 0

    return data.get("data", {}).get("subscribers", 0)
