#!/usr/bin/env python3
""""duck type an iterable object"""
from typing import Tuple, List, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns a list of values with their length"""
    return [(i, len(i)) for i in lst]
