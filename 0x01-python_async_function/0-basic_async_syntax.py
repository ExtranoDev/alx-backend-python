#!/usr/bin/env python3
"""Basics of Async"""
import asyncio
import random


async def wait_random(max_delay: int = 10):
    """asynchronous coroutine that takes
       Args(max_delay, default: 10)
       waits for a random delay between 0 and max_delay
    """
    r = random.uniform(0, max_delay)
    await asyncio.sleep(r)
    return r
