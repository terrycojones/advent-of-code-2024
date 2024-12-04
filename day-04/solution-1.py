#!/usr/bin/env python

import sys


def count_horizontal(a):
    n_cols = len(a[0])
    count = 0
    for row in a:
        for col in range(n_cols - 3):
            word = "".join(row[col : col + 4])
            count += word in {"XMAS", "SAMX"}

    return count


def count_diagonal(a):
    n_rows = len(a)
    n_cols = len(a[0])
    count = 0
    for row in range(n_rows - 3):
        for col in range(n_cols - 3):
            word = "".join(a[row + i][col + i] for i in range(4))
            count += word in {"XMAS", "SAMX"}

    return count


original = []
for line in sys.stdin:
    original.append(list(line.strip()))

rotated = list(zip(*original[::-1]))

count = 0
for data in original, rotated:
    count += count_horizontal(data) + count_diagonal(data)

print(count)
