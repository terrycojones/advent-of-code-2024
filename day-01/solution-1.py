#!/usr/bin/env python

a = []
b = []

for line in open("input-1.txt"):
    a1, b1 = map(int, line.split())
    a.append(a1)
    b.append(b1)

print(sum(abs(a1 - b1) for a1, b1 in zip(sorted(a), sorted(b))))
