#!/usr/bin/python3
"""Create a class BasicCache that inherits
from BaseCaching and is a caching system:
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A basic cache with limited capacity."""
    def put(self, key, item):
        """assign to the dictionary"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key is None or self.cache_data[key] is None:
            return None
        self.cache_data.get(key)
