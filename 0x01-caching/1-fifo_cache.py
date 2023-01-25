#!/usr/bin/env python3
"""FIFO Cache"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Fifo cache class"""

    def __init__(self):
        """Init"""
        super().__init__()
        self.aux_list = []

    def put(self, key, item):
        """
        If the key and item are not empty, add the key and item
        to the cache_data dictionary and append the
        key to the aux_list. If the length of the cache_data
        dictionary is greater than the MAX_ITEMS
        constant, delete the first item in the cache_data
        dictionary and remove the first item in the
        aux_list.

        :param key: the key to be added to the cache
        :param item: the item to be added to the cache
        """
        if key and item:
            self.cache_data[key] = item
            self.aux_list.append(key)
            if self.cache_data.__len__() > BaseCaching.MAX_ITEMS:
                print(f'DISCARD: {self.aux_list[0]}')
                del self.cache_data[self.aux_list[0]]
                self.aux_list.pop(0)

    def get(self, key):
        """
        If the key is in the cache and the cache is not empty,
        return the value of the key

        :param key: The key to be stored in the cache
        :return: The value of the key in the cache_data dictionary.
        """
        if key in self.cache_data and self.cache_data.__len__() > 0:
            return self.cache_data[key]
        return None
