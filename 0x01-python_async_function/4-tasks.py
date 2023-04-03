#!/usr/bin/env python3
"""Handles Tasks"""
import asyncioi
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Calls task_wait_random to check task random time"""
    delays = []
    for i in range(n):
        delays.append(await task_wait_random(max_delay))
    return sorted(delays)
