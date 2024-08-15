#!/usr/bin/env python3
"""
Main file to test Cache class functionality.
"""

from exercise import Cache

cache = Cache()

# Store some values and print the stored keys
s1 = cache.store("first")
print(s1)
s2 = cache.store("second")
print(s2)
s3 = cache.store("third")
print(s3)

# Retrieve and print the input history
inputs = cache._redis.lrange(
    "{}:inputs".format(cache.store.__qualname__), 0, -1
)
outputs = cache._redis.lrange(
    "{}:outputs".format(cache.store.__qualname__), 0, -1
)

print("inputs: {}".format(inputs))
print("outputs: {}".format(outputs))

# Replay the history of the store method
cache.replay(cache.store)
