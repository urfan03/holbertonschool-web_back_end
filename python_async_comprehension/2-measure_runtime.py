#!/usr/bin/env python3
"""Import async_comprehension from the previous file
        and write a measure_runtime coroutine that will
        execute async_comprehension four times in parallel
        using asyncio.gather.
        measure_runtime should measure the total runtime and return it.
        Notice that the total runtime is roughly 10 seconds,
        explain it to yourself.
"""

from asyncio import gather
from time import time


async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """measure_runtime should measure the total runtime """
    tasks = []
    start_time = time()
    for i in range(4):
        await gather(async_comprehension(), async_comprehension(),
                 async_comprehension(), async_comprehension())
    end_time = time()
    return  end_time - start_time
