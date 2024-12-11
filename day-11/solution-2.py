#!/usr/bin/env python

from functools import cache
from utils import blink1, getData


@cache
def blink(stone, n):
    if n == 0:
        return 1
    else:
        return sum(blink(child, n - 1) for child in blink1(stone))


stones, iterations = getData()

print(sum(blink(stone, iterations) for stone in stones))
