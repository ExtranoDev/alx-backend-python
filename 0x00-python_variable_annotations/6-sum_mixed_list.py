#!/usr/bin/env python3
"""Complex types - mixed list"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """takes a list of floats as argument
    returns their sum as a float"""
    return sum(mxd_list)
