#!/usr/bin/env python3
"""Handles Tasks"""
from asyncio import create_task, Task


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """ takes an integer max_delay and returns a asyncio.Task"""
    return create_task(wait_random(max_delay))