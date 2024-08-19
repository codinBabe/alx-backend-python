#!/usr/bin/env python3
""" Tasks """


from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Wait for a random delay n times """
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)
    return delays