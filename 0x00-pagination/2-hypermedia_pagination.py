#!/usr/bin/env python3
""" hypermedia_pagination """
from typing import List
import math
import csv
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        It reads the data file and returns the data as a list of lists
        :return: A list of lists.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

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
        assert type(page) is int, "Page number must be an integer"
        assert type(page_size) is int, "Page size must be an integer"
        assert page > 0, "Page number must be greater than 0"
        assert page_size > 0, "Page size must be greater than 0"
        dataset = self.dataset()
        indexes = index_range(page, page_size)
        return dataset[indexes[0]: indexes[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        > The function takes in a page number and a page size, and returns
        a dictionary with the data for that page, the next page, the previous
        page, the total number of pages, and the page size

        :param page: The page number to return, defaults to 1
        :type page: int (optional)
        :param page_size: The number of items to return per page,
        defaults to 10
        :type page_size: int (optional)
        :return: A dictionary with the following keys:
            - page_size
            - page
            - data
            - next_page
            - prev_page
            - total_pages
        """
        response = {}
        response['page_size'] = page_size
        response['page'] = page
        response['data'] = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        response['next_page'] = None if total_pages == page else page + 1
        response['prev_page'] = None if page == 1 else page - 1
        response['total_pages'] = total_pages
        return response
