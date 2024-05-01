#!/usr/bin/env python3
""" DOcumentation """

import redis
from uuid import uuid4
from functools import wraps
from typing import Union, Callable


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts the number of times a method is called.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: The decorated method.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """
    Represents a cache that stores data in Redis.

    Attributes:
        _redis (redis.Redis): The Redis connection object.
    """

    def __init__(self):
        """
        Initializes a new instance of the Cache class.
        It creates a connection to Redis and flushes the Redis database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the given data in Redis with a randomly generated key.

        Args:
            data (Union[str, bytes, int, float]): The data to be stored.

        Returns:
            str: The randomly generated key used to store the data in Redis.
        """
        randomkey = str(uuid4())
        self._redis.set(randomkey, data)
        return randomkey

    def get(self, key: str,
            fn: Callable = None) -> Union[str, bytes, float, int, None]:
        """
        Retrieves the data stored in Redis with the specified key.

        Args:
            key (str): The key used to store the data in Redis.
            fn : A function to apply to the retrieved data. Defaults to None.

        Returns:
            The retrieved data,
            optionally transformed by the provided function.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> str:
        """
        Retrieves a string value stored in Redis with the specified key.

        Args:
            key (str): The key used to store the string value in Redis.

        Returns:
            str: The retrieved string value.
        """
        return self.get(key, fn=lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """
        Retrieves an integer value stored in Redis with the specified key.

        Args:
            key (str): The key used to store the integer value in Redis.

        Returns:
            int: The retrieved integer value.
        """
        return self.get(key, fn=lambda x: int(x))
