#!/usr/bin/env python3

""" LIFO Cache """

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFO cache class"""

    def __init__(self):
        """ Initialization """
        super().__init__()
        self.aux_list = []

    def put(self, key, value):
        """
        If the key and value are not empty, add the key and value to the
        cache_data dictionary and append  the key to the aux_list.
        If the length of the cache_data dictionary is greater than the
        MAX_ITEMS, delete the last item in the aux_list from the cache_data
        dictionary

        :param key: the key to be added to the cache
        :param value: the value to be stored in the cache
        """
        if key and value:
            self.cache_data[key] = value
            self.aux_list.append(key)
            if self.cache_data.__len__() > BaseCaching.MAX_ITEMS:
                print(f'DISCARD: {self.aux_list[-2]}')
                del self.cache_data[self.aux_list[-2]]

    def get(self, key):
        """
        If the key is in the cache, return the value, otherwise return None

        :param key: The key to store the data under
        :return: The value of the key in the cache_data dictionary.
        """
        if key in self.cache_data and self.cache_data.__len__() > 0:
            return self.cache_data[key]
        return None
