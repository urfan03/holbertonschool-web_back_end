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
