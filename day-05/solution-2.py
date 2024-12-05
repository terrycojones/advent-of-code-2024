#!/usr/bin/env python

from collections import Counter
from utils import readData, valid

rules, inputs = readData()
total = 0

for i in inputs:
    if not valid(i, rules, set()):
        before = Counter()
        for rule in rules:
            if not set(rule) - set(i):
                before[rule[1]] += 1

        new = sorted(i, key=lambda page: before[page])
        total += new[len(new) >> 1]

print(total)
