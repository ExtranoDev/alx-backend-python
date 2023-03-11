#!/usr/bin/env python3
"""Complex types - string and int/float to tuple"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """args: k(str), v: can be an in of float
    returns a tuple containing string and square of number"""
    return k, v * v