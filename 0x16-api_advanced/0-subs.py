import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API for the number of subscribers
    of a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers of the subreddit,
        or 0 if the subreddit is invalid.
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0(by /u/oreosinit)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for error responses

        data = response.json()
        return data.get("data", {}).get("subscribers", 0)

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            return 0  # Subreddit not found
        else:
            raise  # Re-raise other errors
