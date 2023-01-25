#!/usr/bin/env python3
""" MRU Cache """

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ CLASS MRU Cache """

    def __init__(self):
        """ Initialize MRU Cache """
        super().__init__()
        self.aux_list = []

    def put(self, key, item):
        """
        If the key and item are not empty, then if the key is in the cache,
        remove it from the aux_list, add the key and item to the cache,
        append the key to the aux_list, and if the cache is larger than the
        max items, print the first item in the aux_list, and if the key is
        in the cache, delete the first item in the aux_list and pop it from
        the aux_list.

        :param key: the key to be added to the cache
        :param item: the item to be added to the cache
        """
        if key and item:
            if self.cache_data.__len__() >= BaseCaching.MAX_ITEMS:
                last_item = self.aux_list.pop()
                print(f'DISCARD: {last_item}')
                del self.cache_data[last_item]
            self.cache_data[key] = item
            self.aux_list.append(key)

    def get(self, key):
        """
        If the key is in the cache, move it to the front of the list and
        return the value

        :param key: The key to be searched in the cache
        :return: The value of the key in the cache_data dictionary.
        """
        if key in self.cache_data and key:
            self.aux_list.remove(key)
            self.aux_list.append(key)
            return self.cache_data[key]
        return None
