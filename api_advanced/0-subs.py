#!/usr/bin/python3
"""
Return the number of subscribers for a subreddit.

Prototype: def number_of_subscribers(subreddit)

If the subreddit is invalid or an error occurs, return 0.

Notes:
- Uses the Reddit endpoint: /r/<subreddit>/about.json
- Do not follow redirects (allow_redirects=False)
- Provide a custom User-Agent to avoid rate limits
"""
import requests


def number_of_subscribers(subreddit):
    """
    Return total subscribers for a subreddit, or 0 on failure.
    """
    if not subreddit or not isinstance(subreddit, str):
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "python:0-subs:v1.0 (by /u/shyakafrancis123)"}

    try:
        resp = requests.get(url, headers=headers,
                            allow_redirects=False, timeout=10)
    except requests.RequestException:
        return 0

    if resp.status_code != 200:
        return 0

    try:
        data = resp.json()
    except ValueError:
        return 0

    return data.get("data", {}).get("subscribers", 0)
