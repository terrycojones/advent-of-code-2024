#!/usr/bin/env python

import sys
import numpy as np
from collections import defaultdict


grid = np.array([tuple(map(int, line.strip())) for line in sys.stdin.readlines()])
counts = np.zeros(grid.shape, dtype=int)
reachable = defaultdict(set)
nrows, ncols = grid.shape


def count_upward(value, row, col):
    for r, c in (row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col):
        if 0 <= r < nrows and 0 <= c < ncols and grid[r, c] == value + 1:
            if value == 8:
                counts[row, col] += 1
                reachable[(row, col)].add((r, c))
            else:
                counts[row, col] += counts[r, c]
                reachable[(row, col)].update(reachable[(r, c)])


for value in range(8, -1, -1):
    [count_upward(value, row, col) for row, col in np.argwhere(grid == value)]

result1 = result2 = 0

for row, col in np.argwhere(grid == 0):
    result1 += len(reachable[(row, col)])
    result2 += counts[row, col]

print("Solution 1:", result1)
print("Solution 2:", result2)
