#!/usr/bin/env python3
""" Simple helper function """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    "Return a range of indexes for a given page and page size."
    :param page: The page number to return
    :type page: int
    :param page_size: The number of items to return per page
    :type page_size: int
    :return: A range object
    """
    result: int = page * page_size
    return (result - page_size, result)
