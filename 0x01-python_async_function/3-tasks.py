#!/usr/bin/env python3
"""Tasks module"""
wait_random = __import__("0-basic_async_syntax").wait_random

import asyncio
import time


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns a asyncio.Task"""
    return asyncio.create_task(wait_random(max_delay))
