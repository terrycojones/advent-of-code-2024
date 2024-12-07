#!/usr/bin/env python

import numpy as np
from utils import readGrid, find


def countLocations(grid):
    ncols = grid.shape[1]
    grow, gcol = find(grid)
    locations = set()
    rotations = 0

    while grow:
        assert grid[grow, gcol] == "^"
        orig = find(np.rot90(grid, -(rotations % 4)))
        if grid[grow - 1, gcol] == "#":
            grid = np.rot90(grid)
            rotations += 1
            or_, oc = grow, gcol
            grow = ncols - oc - 1
            gcol = or_
        else:
            grid[grow, gcol] = "."
            grow -= 1
            grid[grow, gcol] = "^"

        locations.add(orig)

    orig = find(np.rot90(grid, -(rotations % 4)))
    locations.add(orig)

    return len(locations)


print(countLocations(readGrid()))
