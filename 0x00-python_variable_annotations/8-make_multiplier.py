#!/usr/bin/env python3
"""Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """args: multiplier(float)
    returns a callable object"""

    def mult_call(val: float) -> float:
        """multiplier function call"""
        return val * multiplier
    return mult_call
