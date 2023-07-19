#!/usr/bin/env python3
"""
module to create a redis  class
"""
import uuid
import redis


class Cache:
    """
    A redis class aimed for caching
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: any) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
