#!/usr/bin/env python

from operator import add, mul
from dark.dimension import dimensionalIterator
from utils import solve


def concat(a, b):
    return int(f"{a}{b}")


def perms(n):
    for p in dimensionalIterator([3] * n):
        yield [add if c == 0 else (mul if c == 1 else concat) for c in p]


solve(perms)
