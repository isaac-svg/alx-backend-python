#!/usr/bin/env python3

import asyncio
from typing import Coroutine

wait_random = __import__('1-concurrent_coroutines').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    coroutine: Coroutine = wait_random(max_delay)
    return asyncio.create_task(coroutine)
