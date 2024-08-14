#!/usr/bin/env python3

from typing import Callable, Optional, Union
from uuid import uuid4
import redis
from functools import wraps

"""
This module provides a Cache class for storing and retrieving data
in a Redis database. It includes decorators for tracking method calls,
logging function input/output history, and replaying function calls.
"""


def track_calls(func: Callable) -> Callable:
    """
    Decorator that tracks how many times a function is called.

    Args:
        func: The function to be decorated.

    Returns:
        The decorated function with call counting.
    """

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        """
        Increments the call count each time the function is called.

        Args:
            self: The instance of the Cache class.
            *args: Positional arguments for the function.
            **kwargs: Keyword arguments for the function.

        Returns:
            The result of the original function call.
        """
        func_name = func.__qualname__
        self._redis.incr(func_name)
        return func(self, *args, **kwargs)

    return wrapper


def log_history(func: Callable) -> Callable:
    """
    Decorator that logs the history of inputs and outputs
    for a function.

    Args:
        func: The function to be decorated.

    Returns:
        The decorated function with input/output logging.
    """
    func_name = func.__qualname__
    input_log = func_name + ":inputs"
    output_log = func_name + ":outputs"

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        """
        Logs the inputs and outputs of the function.

        Args:
            self: The instance of the Cache class.
            *args: Positional arguments for the function.
            **kwargs: Keyword arguments for the function.

        Returns:
            The result of the original function call.
        """
        self._redis.rpush(input_log, str(args))
        result = func(self, *args, **kwargs)
        self._redis.rpush(output_log, str(result))
        return result

    return wrapper


def display_history(func: Callable) -> None:
    """
    Displays the recorded history of inputs and outputs for a function.

    Args:
        func: The function whose history is to be displayed.

    Returns:
        None
    """
    func_name = func.__qualname__
    cache = redis.Redis()
    call_count = cache.get(func_name).decode("utf-8")
    print(f"{func_name} was called {call_count} times:")

    input_log = cache.lrange(f"{func_name}:inputs", 0, -1)
    output_log = cache.lrange(f"{func_name}:outputs", 0, -1)

    for input_data, output_data in zip(input_log, output_log):
        print(f"{func_name}(*{input_data.decode('utf-8')}) -> "
              f"{output_data.decode('utf-8')}")


class Cache:
    """
    Cache class for interacting with Redis to store and retrieve data.
    """

    def __init__(self):
        """
        Initializes the Cache instance with a Redis connection and
        clears the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @track_calls
    @log_history
    def save(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores data in Redis with a randomly generated key.

        Args:
            data: The data to store, which can be a string, bytes, int,
                  or float.

        Returns:
            The key under which the data is stored.
        """
        unique_key = str(uuid4())
        self._redis.set(unique_key, data)
        return unique_key

    def retrieve(self, key: str, transformer: Optional[Callable] = None) \
            -> Union[str, bytes, int, float]:
        """
        Retrieves data from Redis and optionally applies a transformation.

        Args:
            key: The key associated with the stored data.
            transformer: An optional callable to transform the data.

        Returns:
            The retrieved data, possibly transformed.
        """
        value = self._redis.get(key)
        if transformer:
            value = transformer(value)
        return value

    def retrieve_str(self, key: str) -> str:
        """
        Retrieves and decodes a string from Redis.

        Args:
            key: The key associated with the stored string.

        Returns:
            The retrieved string.
        """
        value = self._redis.get(key)
        return value.decode("utf-8")

    def retrieve_int(self, key: str) -> int:
        """
        Retrieves an integer from Redis.

        Args:
            key: The key associated with the stored integer.

        Returns:
            The retrieved integer, or 0 if conversion fails.
        """
        value = self._redis.get(key)
        try:
            return int(value.decode("utf-8"))
        except Exception:
            return 0
