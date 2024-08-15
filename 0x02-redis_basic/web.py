#!/usr/bin/env python3
"""
Module to cache HTML content from URLs and track access count using Redis.

The `get_page` function fetches the HTML content of a URL, caches it with a
10-second expiration, and tracks how many times the URL was accessed.
"""

import redis
import requests
from typing import Optional

# Initialize the Redis client
r = redis.Redis()


def get_page(url: str) -> Optional[str]:
    """
    Fetches the HTML content of a URL, caches it in Redis with a 10-second
    expiration, and tracks how many times the URL has been accessed.

    Args:
        url (str): The URL to fetch the HTML content from.

    Returns:
        Optional[str]: The HTML content of the page.
    """
    # Track URL access count
    access_count_key = f"count:{url}"
    r.incr(access_count_key)

    # Check if the URL's page is cached
    cached_page_key = f"cached:{url}"
    cached_page = r.get(cached_page_key)

    if cached_page:
        return cached_page.decode('utf-8')

    try:
        # Fetch the page if not cached
        response = requests.get(url)
        response.raise_for_status()  # Ensure the request was successful
        html_content = response.text

        # Cache the result with a 10-second expiration
        r.setex(cached_page_key, 10, html_content)
        return html_content
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None


# Example usage
if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk"
    print(get_page(url))  # First call fetches and caches
    print(get_page(url))  # Second call uses the cache
