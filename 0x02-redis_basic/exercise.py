#!/usr/bin/env python3
"""
Module to interact with Redis and store/retrieve data.
"""

from typing import Union
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
