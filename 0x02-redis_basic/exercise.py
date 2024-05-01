#!/usr/bin/env python3
""" DOcumentation """

import redis
from uuid import uuid4
from typing import Union


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
