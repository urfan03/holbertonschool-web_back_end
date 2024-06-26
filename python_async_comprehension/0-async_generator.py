#!/usr/bin/env python3
"""Write a coroutine called async_generator
   that takes no arguments."""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """The coroutine will loop 10 times"""
    for i in range(10):
        await asyncio.sleep(1)
        yield 10 * random.random()
