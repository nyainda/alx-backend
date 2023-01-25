#!/usr/bin/python3
''' LFUCache '''


BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    ''' LFU Cache '''

    def __init__(self):
        ''' Initialize LFUCache '''
        self.aux_list = []
        self.aux_dict = {}
        super().__init__()

    def _get_less_frequency(self):
        """
        It returns the minimum value of the dictionary.
        :return: The minimum value in the dictionary.
        """
        return min(self.aux_dict.values())

    def put(self, key, item):
        """
        If the key and item are not empty, and the cache is full,
        remove the least frequently used item, and add the new key and item
        to the cache

        :param key: the key to be added to the cache
        :param item: the item to be added to the cache
        """
        if key and item:
            if self.cache_data.__len__() >= BaseCaching.MAX_ITEMS:
                less_frequency = self._get_less_frequency()
                keys_with_less_frequency = [key for key, value
                                            in self.aux_dict.items()
                                            if value == less_frequency]
                if keys_with_less_frequency.__len__() > 1:
                    keys_with_less_frequency.sort()
                    key_to_remove = keys_with_less_frequency[0]
                else:
                    key_to_remove = keys_with_less_frequency[0]
                self.aux_list.remove(key_to_remove)
                del self.aux_dict[key_to_remove]
                del self.cache_data[key_to_remove]
                print(f'DISCARD: {key_to_remove}')

            if self.aux_dict.get(key):
                self.aux_dict[key] += 1
            else:
                self.aux_dict[key] = 1

            self.aux_list.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        If the key is in the cache, then return the value of the key

        :param key: The key to be searched in the cache
        :return: The value of the key in the cache_data dictionary.
        """
        if key in self.cache_data and key:
            self.aux_dict[key] += 1
            self.aux_list.remove(key)
            self.aux_list.append(key)
            return self.cache_data[key]
