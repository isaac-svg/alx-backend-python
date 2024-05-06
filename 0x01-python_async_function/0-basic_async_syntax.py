#!/usr/bin/env python3

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
        Asynchronous function that awaits a result based on a delay

        Args:
        max_delay: an Interger value that speciefies the maximum time the function will sleep
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
