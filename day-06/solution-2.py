#!/usr/bin/env python

import numpy as np
from utils import readGrid, find

UP, DOWN, LEFT, RIGHT = range(4)
OUTSIDE, BLOCKED, LOOPING, ACTIVE = range(4)


class Grid:
    def __init__(self):
        self.orig = readGrid()
        self.row, self.col = find(self.orig)
        self.orig_row, self.orig_col = self.row, self.col
        self.nrows, self.ncols = self.orig.shape
        self.max_row, self.max_col = self.nrows - 1, self.ncols - 1
        self.reset()

    def reset(self):
        self.grid = np.array(self.orig)
        self.row, self.col = self.orig_row, self.orig_col
        self.direction = UP
        self.blockStates = set()
        self.locations = set()
        self.addLocation()
        self.state = None
        self.setState()

    def setState(self):
        if self.direction == UP:
            if self.row == 0:
                self.state = OUTSIDE
            elif self.grid[self.row - 1, self.col] == "#":
                self.state = BLOCKED
            else:
                self.state = ACTIVE

        elif self.direction == DOWN:
            if self.row == self.max_row:
                self.state = OUTSIDE
            elif self.grid[self.row + 1, self.col] == "#":
                self.state = BLOCKED
            else:
                self.state = ACTIVE

        elif self.direction == LEFT:
            if self.col == 0:
                self.state = OUTSIDE
            elif self.grid[self.row, self.col - 1] == "#":
                self.state = BLOCKED
            else:
                self.state = ACTIVE

        elif self.direction == RIGHT:
            if self.col == self.max_col:
                self.state = OUTSIDE
            elif self.grid[self.row, self.col + 1] == "#":
                self.state = BLOCKED
            else:
                self.state = ACTIVE

        else:
            raise ValueError("WTF")

        if self.state == BLOCKED:
            blockedState = (self.row, self.col, self.direction)
            if blockedState in self.blockStates:
                self.state = LOOPING
            else:
                self.blockStates.add(blockedState)

    def addLocation(self):
        self.locations.add((self.row, self.col))

    def run1(self):
        if self.state == OUTSIDE:
            raise ValueError("Cannot move - already outside!")

        if self.state == LOOPING:
            raise ValueError("Cannot move - looping!")

        elif self.state == BLOCKED:
            if self.direction == UP:
                self.direction = RIGHT
            elif self.direction == DOWN:
                self.direction = LEFT
            elif self.direction == LEFT:
                self.direction = UP
            elif self.direction == RIGHT:
                self.direction = DOWN

            self.setState()

        else:
            rowinc = colinc = 0
            if self.direction == UP:
                assert self.row > 0
                rowinc = -1
            elif self.direction == DOWN:
                assert self.row < self.max_row
                rowinc = 1
            elif self.direction == LEFT:
                assert self.col > 0
                colinc = -1
            elif self.direction == RIGHT:
                assert self.col < self.max_col
                colinc = 1

            assert self.grid[self.row, self.col] == "^"
            self.grid[self.row, self.col] = "."
            self.row, self.col = self.row + rowinc, self.col + colinc
            assert self.grid[self.row, self.col] == "."
            self.grid[self.row, self.col] = "^"

            self.addLocation()
            self.setState()

    def countLocations(self):
        while self.state != OUTSIDE:
            self.run1()
        return len(self.locations)

    def countBlockers(self):
        count = 0
        for row in range(self.nrows):
            for col in range(self.ncols):
                self.reset()
                if self.grid[row, col] == ".":
                    self.grid[row, col] = "#"
                    self.setState()
                    while True:
                        if self.state == OUTSIDE:
                            break
                        elif self.state == LOOPING:
                            # print(row, col, "creates a loop")
                            count += 1
                            break
                        else:
                            self.run1()

        return count


# Using the countLocations method for problem 1 is _much_ faster than the
# solution in solution-1.py
#
# print(Grid().countLocations())

print(Grid().countBlockers())
