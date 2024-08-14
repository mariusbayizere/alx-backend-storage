# Redis-based Cache Implementation

This project demonstrates the implementation of a Redis-based caching system using Python 3.7 on Ubuntu 18.04 LTS. The project includes several tasks that showcase various features of Redis and Python's type annotations, decorators, and documentation practices.

## Requirements

- All files are interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- All files end with a new line.
- The first line of all files is exactly `#!/usr/bin/env python3`.
- The code adheres to the pycodestyle style (version 2.5).
- All modules, classes, and methods are documented properly.
- All functions and coroutines are type-annotated.

## Setup

### Install Redis

To install Redis on Ubuntu 18.04 LTS, run the following commands:

```bash
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sudo sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
Start Redis Server
If using Redis in a container, the server is stopped by default. Start it with:

bash
Copy code
$ service redis-server start
Tasks
0. Writing Strings to Redis
Implement a Cache class that initializes a Redis client.
Create a store method that stores data in Redis with a randomly generated key.
The store method is type-annotated to handle str, bytes, int, and float.
1. Reading from Redis and Recovering Original Type
Implement a get method in the Cache class that retrieves data from Redis.
The get method can take a callable to convert the data back to its original type.
Implement get_str and get_int methods that parametrize the get method with appropriate conversion functions.
2. Incrementing Values
Create a count_calls decorator to count how many times methods of the Cache class are called.
Use the __qualname__ of the method as the key in Redis to store the count.
Decorate the store method with count_calls.
3. Storing Lists
Implement a call_history decorator to store the history of inputs and outputs for a particular function.
Store input arguments and output values in separate Redis lists.
4. Retrieving Lists
Implement a replay function to display the history of calls for a particular function.
