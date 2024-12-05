#!/usr/bin/env python

from utils import readData, valid

rules, inputs = readData()
total = 0

for i in inputs:
    if valid(i, rules, set()):
        total += i[len(i) >> 1]

print(total)
