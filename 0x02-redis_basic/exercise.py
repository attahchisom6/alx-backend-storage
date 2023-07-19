#!/usr/bin/env python3
"""
module to create a redis  class
"""
import uuid
import redis
from typing import Union, Callable, Optional


class Cache:
    """
    A redis class aimed for caching
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None)
    -> [str, bytes, int, float]:
        """
        this method takes a string key and a callable, the callable
        take a str as an argument and can return a str, byte, int, float
        """
        value = self._redis.get(key)
        if value is None:
            return None
        return fn(value)

    def get_str(self, key: str) -> str:
        """
        parameterize the return of get to str
        """
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """
        parameterize the return of get to int
        """
        return self.get(key, int)
