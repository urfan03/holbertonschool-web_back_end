#!/usr/bin/env python3
'''
Create a measure_time function with integers n and max_delay as arguments
'''

from asyncio import run
from time import time

wait_n = __import__('1-cocurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Use the time module to measure an approximate elapsed time."""
    time_1 = time()
    run(wait_n(n, max_delay))
    time_2 = time()
    elapsed_time = time_2 - time_1
    return elapsed_time / n
