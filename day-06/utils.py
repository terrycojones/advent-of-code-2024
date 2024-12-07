import sys
import numpy as np


def readGrid():
    return np.array([tuple(line.strip()) for line in sys.stdin.readlines()])


def find(grid):
    nrows, ncols = grid.shape
    for row in range(nrows):
        for col in range(ncols):
            if grid[row, col] == "^":
                return row, col
