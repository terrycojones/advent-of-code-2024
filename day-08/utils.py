import sys
import numpy as np
from collections import defaultdict


def readGrid():
    grid = np.array([tuple(line.strip()) for line in sys.stdin.readlines()])
    nrows, ncols = grid.shape
    data = defaultdict(list)
    for row in range(nrows):
        for col in range(ncols):
            if grid[row, col].isalnum():
                data[grid[row, col]].append((row, col))

    return data, nrows, ncols
