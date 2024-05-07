#!/usr/bin/env python3

"""
An async generator function
"""

import random
import asyncio
from typing import AsyncGenerator, Any


async def async_generator() -> AsyncGenerator[Any, Any]:
    """
    Loops ten times and for each iteration yields
    a random number
    Returns:
    a radom number
    """
    for i in range(10):
        await  asyncio.sleep(1)
        yield random.uniform(0, 10)
