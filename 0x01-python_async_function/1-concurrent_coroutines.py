#!/usr/bin/env python3

from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio

async def wait_n(n: int, max_delay:int) -> List[float]:
    """
        Gathers  n number of calls of wait_random in a list and returns it as sorted

        Args:
        n(int): Number of times to call wait_random
        max_delay(int): Maximum delay for each wait_random call
    """
    delays =  await asyncio.gather(*(wait_random(max_delay) for i in range(n)))
    return sorted(delays)
