#!/usr/bin/env python3

"""
Measures time taken to call n asynchronous coroutines
"""

import asyncio
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
        Measures time taken for the wait_n to run n
        wait_random calls with maximum delay of
        max_delay
        Args:
        n(int):
        number of times wait_n will call its internal function
        max_delay(int):
        maximum delay fro each function call
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
