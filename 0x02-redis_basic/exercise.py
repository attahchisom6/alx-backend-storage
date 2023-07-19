#!/usr/bin/env python3
"""
module to create a redis  class
"""
import uuid
import redis
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    """
    count how many timea the cache class is called and returns a callable
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        function that increments the count for the key every time the method is
        called and returns the value returned by the original method.
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """
    decorator to store the history of inputs and outputs for a particular function (Callable
    """
    inputs = []
    outphts = []
    input_key = ":inputs"
    output_key = ":outputs"

    @wraps(method)
    @wrapper(self, *args):
        """
        wrapper to return a function
        """
        self._redis.rpush inputs str(args)
        results = method(self, *args)
        return self._redis.rpush outputs result
    return wrapper


class Cache:
    """
    A redis class aimed for caching
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @history_calls
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        this method takes a string key and a callable, the callable
        take a str as an argument and can return a str, byte, int, float
        """
        value = self._redis.get(key)
        if fn:
            return fn(value)
        return value

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
