#!/usr/bin/env python3
""" Basic cache """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Basic Cache that inherits from base_cache

    Args:
        BaseCaching (Class): Class to handle cache
    """

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data and self.cache_data[key]:
            return self.cache_data[key]
        return None
