#!/usr/bin/env python

from operator import add, mul
from utils import solve


def perms(n):
    for s in (f"{x:0{n}b}" for x in range(1 << n)):
        yield [add if c == "0" else mul for c in s]


solve(perms)
