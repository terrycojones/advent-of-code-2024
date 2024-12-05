#!/usr/bin/env python

from utils import readData, valid

rules, inputs = readData()
total = 0

for i in inputs:
    if not valid(i, rules, set()):
        applicable_rules = []
        for rule in rules:
            if not set(rule) - set(i):
                applicable_rules.append(rule)

        def key(page):
            return sum(page == rule[1] for rule in applicable_rules)

        new = sorted(i, key=key)
        assert valid(new, rules, set())
        total += new[len(new) >> 1]

print(total)
