#!/usr/bin/env python

from collections import Counter

a = []
b = Counter()

for line in open("input-1.txt"):
    a1, b1 = map(int, line.split())
    a.append(a1)
    b[b1] += 1

print(sum(a1 * b[a1] for a1 in a))
