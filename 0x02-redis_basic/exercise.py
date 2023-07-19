#!/usr/bin/env python3
"""
module to create a redis  class
"""
import uuid
import redis
from typing import Union, Callable


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

    def get(key: str, fn: Callable[None]) -> UnionOfTypes:
        if key is None:
            return None
        def fn(key: str) -> UnionOfTypes:
            """
            return a converted data
            """
            return key.converted()
        return fn(key)

    def get_str(self):
        """
        parameterize get to str
        """
        return str(Cache.get())

    def get_int(self):
        """
        parameterize the return of get into int
        """
        return int(cache.get())
