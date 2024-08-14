#!/usr/bin/env python3
"""Module for caching webpage content and tracking access counts using Redis.

This module provides functionality to cache the content of a webpage and
track how many times a specific URL has been accessed. The caching is managed
using Redis, and a decorator simplifies the process.
"""
import redis
import requests
from functools import wraps
from typing import Callable


redis_client = redis.Redis()
"""Redis instance for managing cached data and tracking access counts."""


def cache_decorator(
        func: Callable[[str], str]
) -> Callable[[str], str]:
    """Decorator to cache webpage content and track URL access counts.

    Args:
        func (Callable[[str], str]): The function to be decorated, which
                                      fetches the webpage content.

    Returns:
        Callable[[str], str]: The wrapper function that handles caching and
                               access counting.
    """

    @wraps(func)
    def wrapper(url: str) -> str:
        """Wrapper function to manage caching and access counting.

        Args:
            url (str): The URL of the webpage to be fetched and cached.

        Returns:
            str: The HTML content of the requested webpage.
        """
        # Increment the access count for the given URL
        redis_client.incr(f"count:{url}")

        # Retrieve the cached result if available
        cached_result = redis_client.get(f"result:{url}")
        if cached_result:
            return cached_result.decode("utf-8")

        # Fetch the webpage content if not cached, then cache it
        webpage_content = func(url)
        redis_client.setex(f"result:{url}", 10, webpage_content)
        return webpage_content

    return wrapper


@cache_decorator
def get_page(url: str) -> str:
    """Fetches and returns the HTML content of a webpage.

    This function retrieves the content of a specified URL, caches it for
    10 seconds, and tracks how often the URL is accessed.

    Args:
        url (str): The URL of the webpage to fetch.

    Returns:
        str: The HTML content of the webpage.
    """
    return requests.get(url).text


# Example usage
if __name__ == "__main__":
    test_url = (
        "http://slowwly.robertomurray.co.uk/delay/5000/"
        "url/http://www.example.com"
    )
    print(get_page(test_url))
