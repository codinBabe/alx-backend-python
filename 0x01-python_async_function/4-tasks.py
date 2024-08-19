#!/usr/bin/env python3
""" Tasks """


import asyncio
import time
wait_n = __import__("1-concurrent_coroutines").wait_n
wait_random = __import__("0-basic_async_syntax").wait_random


async def task_wait_n(n:int, max_delay:int) -> float:
    """ Task wait n """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    start = time.time()
    await asyncio.gather(*tasks)
    end = time.time()
    return (end - start) / n