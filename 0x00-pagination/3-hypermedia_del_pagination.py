#!/usr/bin/env python3

"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        It returns a list of lists, where each list is a row of data

        :param page: The page number to return, defaults to 1
        :type page: int (optional)
        :param page_size: The number of items to return per page,
        defaults to 10
        :type page_size: int (optional)
        :return: A list of lists.
        """
        index_range = __import__('0-simple_helper_function').index_range
        assert type(page) is int, "Page number must be an integer"
        assert type(page_size) is int, "Page size must be an integer"
        assert page > 0, "Page number must be greater than 0"
        assert page_size > 0, "Page size must be greater than 0"
        dataset = self.dataset()
        indexes = index_range(page, page_size)
        return dataset[indexes[0]: indexes[1]]

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        > This function returns a dictionary with the current index,
        the next index, the page size, and the data for the current page

        :param index: The index of the first item in the page
        :type index: int
        :param page_size: The number of items to return in the page,
        defaults to 10
        :type page_size: int (optional)
        :return: A dictionary with the index, next_index, page_size, and data.
        """
        response = {
            "index": index,
            "next_index": index + page_size,
            "page_size": page_size,
            "data": self.get_page(index, page_size),
        }
        return response
