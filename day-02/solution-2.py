#!/usr/bin/env python

import sys
from utils import safe


def any_safe(levels):
    return safe(levels) or any(
        safe(levels[:index] + levels[index + 1:]) for index in range(len(levels))
    )

print(sum(any_safe(list(map(int, line.split()))) for line in sys.stdin))
