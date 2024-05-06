#!/usr/bin/env python3

task_wait_random = __import__('3-tasks').task_wait_random
import asyncio

async def task_wait_n(n: int, max_delay:int):
    """
        Gathers  n number of calls of task_wait_random in a list and returns it as sorted

        Args:
        n(int): Number of times to call task_wait_random
        max_delay(int): Maximum delay for each task_wait_random call
    """
    delays =  await asyncio.gather(*(task_wait_random(max_delay) for i in range(n)))
    return sorted(delays)