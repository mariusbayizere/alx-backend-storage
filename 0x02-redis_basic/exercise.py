#!/usr/bin/env python3
"""
Module to interact with Redis and store/retrieve data.
"""

from typing import Union, Callable, Optional
from uuid import uuid4
import redis
import functools


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts the number of times a method is called.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: The decorated method with counting functionality.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function that increments the call count and calls
        the original method.
        """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs for a method.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: The decorated method with history tracking.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function that logs inputs and outputs of the method.
        """
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        # Convert args to a string and store in Redis as inputs
        self._redis.rpush(input_key, str(args))

        # Call the original method and store the result as outputs
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))

        return result

    return wrapper


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

    @count_calls
    @call_history
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
            fn (Callable, optional): A callable used to convert the data
            to the desired format.

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

    def replay(self, method: Callable) -> None:
        """
        Displays the history of calls of a particular function, including
        the inputs and outputs.

        Args:
            method (Callable): The method to retrieve the history for.

        Returns:
            None
        """
        method_name = method.__qualname__
        inputs = self._redis.lrange(f"{method_name}:inputs", 0, -1)
        outputs = self._redis.lrange(f"{method_name}:outputs", 0, -1)

        print(f"{method_name} was called {len(inputs)} times:")
        for inp, outp in zip(inputs, outputs):
            print(f"{method_name}(*{inp.decode('utf-8')}) -> "
                  f"{outp.decode('utf-8')}")
