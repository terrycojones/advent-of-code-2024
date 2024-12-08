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

                    for r, c in zip((row1, row2), (col1, col2)):
                        anti_row = r + row_off
                        anti_col = c + col_off
                        anti = anti_row, anti_col

                        if (
                            0 <= anti_row < nrows
                            and 0 <= anti_col < ncols
                            and anti not in {loc1, loc2}
                        ):
                            antennae.add(anti)

print(len(antennae))
