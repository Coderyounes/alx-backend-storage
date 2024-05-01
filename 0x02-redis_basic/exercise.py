#!/usr/bin/env python3
""" DOcumentation """

import redis
from uuid import uuid4
from typing import Union, Callable


class Cache:
    def __init__(self):
        """
        Initializes a new instance of the Cache class.
        It creates a connection to Redis and flushes the Redis database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the given data in Redis with a randomly generated key.

        Args:
            data: The data to be stored.

        Returns:
            The randomly generated key used to store the data in Redis.
        """
        randomkey = str(uuid4())
        self._redis.set(randomkey, data)
        return randomkey

    def get(self, key: str,
            fn: Callable = None) -> Union[str, bytes, int, float]:
        if fn:
            return fn(key)
        return key

    def get_str(self, key: str) -> str:
        data = self.get(key)
        if isinstance(data, bytes):
            return data.decode('utf-8')
        return str(data)

    def get_int(self, key: str) -> int:
        data = self.get(key)
        if data:
            return int(data)
        else:
            return 0
