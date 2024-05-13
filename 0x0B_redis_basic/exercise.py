#!/usr/bin/env python3
'''Redis module'''
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


class Cache():
    ''' class cache '''
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        ''' store function'''
        gen = str(uuid.uuid4())
        self._redis.set(gen, data)
        return gen

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        '''get function'''
        value = self._redis.get(key)
        return value if not fn else fn(value)

    def get_int(self, key):
        return self.get(key, int)

    def get_str(self, key):
        value = self._redis.get(key)
        return value.decode("utf-8")
