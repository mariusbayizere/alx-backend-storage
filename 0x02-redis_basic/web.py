#!/usr/bin/env python3
"""
This module provides the get_page function to cache web pages and track
URL access counts using Redis. The cache has a 10-second expiration.
"""

import redis
import requests
from typing import Optional
from functools import wraps

# Initialize the Redis client
r = redis.Redis()


def count_access(func):
    """
    Decorator to track how many times a URL has been accessed.

    Args:
        func (Callable): The function to wrap and track accesses for.

    Returns:
        Callable: The wrapped function.
    """
    @wraps(func)
    def wrapper(url: str) -> str:
        key = f"count:{url}"
        r.incr(key)
        return func(url)
    return wrapper


@count_access
def get_page(url: str) -> Optional[str]:
    """
    Fetches the HTML content of a URL and caches it in Redis with a 10-second
    expiration. If the page is cached, it retrieves it from the cache.

    Args:
        url (str): The URL to fetch the HTML content from.

    Returns:
        Optional[str]: The HTML content of the page or None if an error occurs.
    """
    cached_page = r.get(f"cached:{url}")
    if cached_page:
        return cached_page.decode('utf-8')

    try:
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text
        r.setex(f"cached:{url}", 10, html_content)
        return html_content
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None


if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk"
    print(get_page(url))
    print(get_page(url))
