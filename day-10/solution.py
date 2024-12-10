#!/usr/bin/env python

import sys
import numpy as np
from collections import defaultdict


data = np.array([tuple(map(int, line.strip())) for line in sys.stdin.readlines()])
counts = np.zeros(data.shape, dtype=int)
nrows, ncols = data.shape
reachable = defaultdict(set)


def count_upward(value, row, col, grid, counts):
    for rowinc, colinc in ((0, -1), (0, 1), (-1, 0), (1, 0)):
        newrow = row + rowinc
        newcol = col + colinc
        if (
            0 <= newrow < nrows
            and 0 <= newcol < ncols
            and grid[newrow, newcol] == value + 1
        ):
            if value == 8:
                counts[row, col] += 1
                reachable[(row, col)].add((newrow, newcol))
            else:
                counts[row, col] += counts[newrow, newcol]
                reachable[(row, col)].update(reachable[(newrow, newcol)])


for value in range(8, -1, -1):
    for row in range(nrows):
        for col in range(ncols):
            if data[row, col] == value:
                count_upward(value, row, col, data, counts)

result1 = result2 = 0

for row in range(nrows):
    for col in range(ncols):
        if data[row, col] == 0:
            result1 += len(reachable[(row, col)])
            result2 += counts[row, col]

print("Solution 1:", result1)
print("Solution 2:", result2)
