#!/usr/bin/env python3

"""
Asynchronous coroutine that generates n
random delays between 0 and max_delay (inclusive).
"""

from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Gathers  n number of calls of wait_random in a
    list and returns it as sorted

    Args:
        n (int): Number of times to call wait_random
        max_delay (int): Maximum delay for each wait_random call
    Returns:
        list of floats representing time
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for i in range(n)))
    return sorted(delays)
