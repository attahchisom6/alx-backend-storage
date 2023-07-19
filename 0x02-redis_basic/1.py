import uuid
import redis
from typing import Union, Callable

class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable[[str], Union[str, bytes, int, float]]) -> Union[str, bytes, int, float]:
        value = self._redis.get(key)
        if value is None:
            return None
        return fn(value)

    def get_str(self, key: str) -> str:
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        return self.get(key, int)
