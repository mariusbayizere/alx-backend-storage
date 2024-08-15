#!/usr/bin/env python3
"""
This module contains the get_page function to cache web pages and
track access counts.
"""

import redis
import requests
from typing import Optional
from functools import wraps

# Initialize the Redis client
r = redis.Redis()


def count_access(func):
    """
    A decorator to track how many times a URL has been accessed.
    """
    @wraps(func)
    def wrapper(url: str) -> str:
        key = f"count:{url}"
        r.incr(key)  # Increment the count for this URL
        return func(url)
    return wrapper


@count_access
def get_page(url: str) -> Optional[str]:
    """
    Fetch the HTML content of a URL and cache it in Redis with a 10-second
    expiration.

    Args:
        url (str): The URL to fetch the HTML content from.

    Returns:
        str: The HTML content of the URL or None if the request fails.
    """
    # Check if the URL is cached
    cached_page = r.get(f"cached:{url}")
    if cached_page:
        return cached_page.decode('utf-8')

    try:
        # Fetch the page if not cached
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text
        # Cache the result and set it to expire in 10 seconds
        r.setex(f"cached:{url}", 10, html_content)
        return html_content
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None


if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk"
    print(get_page(url))  # First call fetches and caches
    print(get_page(url))  # Second call uses cache
