#!/usr/bin/env python

from utils import readGrid

data, nrows, ncols = readGrid()
antennae = set()

for symbol, locations in data.items():
    if len(locations) > 1:
        for loc1 in locations:
            for loc2 in locations:
                if loc1 != loc2:
                    row1, col1 = loc1
                    row2, col2 = loc2
                    row_off = row1 - row2
                    col_off = col1 - col2

                    for sign in 1, -1:
                        inc = 0
                        while True:
                            anti_row = row1 + sign * row_off * inc
                            anti_col = col1 + sign * col_off * inc

                            if 0 <= anti_row < nrows and 0 <= anti_col < ncols:
                                antennae.add((anti_row, anti_col))
                                inc += 1
                            else:
                                break

print(len(antennae))
