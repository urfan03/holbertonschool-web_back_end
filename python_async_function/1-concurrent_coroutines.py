#!/usr/bin/env python3
'''
Test file for printing the correct output of the wait_n coroutine
'''

import asyncio
import random
wait_n = __import__('1-concurrent_coroutines').wait_n


async def wait_n(n: int, max_delay: int) -> float:
    """list of all the delays"""
    delay = max_delay * random.random()
    await asyncio.sleep(delay)
    return (delay)
