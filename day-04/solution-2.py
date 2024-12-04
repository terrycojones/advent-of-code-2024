#!/usr/bin/env python

import sys


def count_xmas(a):
    n_rows = len(a)
    n_cols = len(a[0])
    count = 0
    for row in range(1, n_rows - 1):
        for i in range(1, n_cols - 1):
            word1 = "".join(a[row + x][i + x] for x in (-1, 0, 1))
            word2 = "".join(a[row + x][i - x] for x in (1, 0, -1))
            count += not ({word1, word2} - {"MAS", "SAM"})

    return count


data = []
for line in sys.stdin:
    data.append(list(line.strip()))

print(count_xmas(data))
