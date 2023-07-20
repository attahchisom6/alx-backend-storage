#!/usr/bin/env python3
"""
module to create a redis  class
"""
import uuid
import redis
from functools import wraps
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
    decorator to store the history of inputs and outputs for a
    particular function (Callable
    """
    key = method.__qualname__
    input_key = "{}:inputs".format(key)
    output_key = "{}:outputs".format(key)

    @wraps(method)
    def wrapper(self, *args):
        """
        wrapper to return a function
        """
        self._redis.rpush(input_key, str(args))
        results = str(method(self, *args))
        self._redis.rpush(output_key, results)
        return results
    return wrapper


def replay(method: Callable) -> None:
    """
    function to display the history of calls of a particular function.
    """
    key = method.__qualname__
    count = Cache.get(key)

    print("Cache.store was called {} times:".format(count))

    input_key = "{}:inputs".format(key)
    output_key = "{}:outputs".format(key)

    inputs = Cache._redis.lrange(input_key, 0, 1)
    outputs = Cache._redis.lrange(output_key, 0, 1)

    for num_calls, (ins, outs) in enumerate(zip(inputs, outputs), 1):
        ins_data = ins.decode()
        outs_data = outs.decode()
        print("{}(*('{}',)) -> {}".format(key, ins_data, outs_data))


class Cache:
    """
    A redis class aimed for caching
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
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
