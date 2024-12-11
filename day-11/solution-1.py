#!/usr/bin/env python

import sys
from utils import blink1, getData


def blink(stones):
    for stone in stones:
        yield from blink1(stone)


stones, iterations = getData()

for i in range(iterations):
    stones = list(blink(stones))

print(len(stones))
