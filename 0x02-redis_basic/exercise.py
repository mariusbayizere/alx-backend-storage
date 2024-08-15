#!/usr/bin/env python3
"""
Module to interact with Redis and store/retrieve data.
"""

from typing import Union, Callable, Optional
from uuid import uuid4
import redis


class Cache:
    """
    Cache class to store and retrieve data from Redis.
    """

    def __init__(self):
        """
        Initializes the Redis client and flushes the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the given data in Redis with a randomly generated key.

        Args:
            data (Union[str, bytes, int, float]): The data to store.

        Returns:
            str: The key under which the data is stored.
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float, None]:
        """
        Retrieves data from Redis using the provided key and an optional
        conversion function.

        Args:
            key (str): The key to retrieve data.
            fn (Callable, optional): A callable used to convert the data to
            the desired format.

        Returns:
            Union[str, bytes, int, float, None]: The retrieved data,
            possibly converted using fn.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieves a string from Redis using the provided key.

        Args:
            key (str): The key to retrieve the string.

        Returns:
            Optional[str]: The retrieved string, or None if key doesn't exist.
        """
        return self.get(key, lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieves an integer from Redis using the provided key.

        Args:
            key (str): The key to retrieve the integer.

        Returns:
            Optional[int]: The retrieved integer, or None if key doesn't exist.
        """
        return self.get(key, int)
