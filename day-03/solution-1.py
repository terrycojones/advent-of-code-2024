#!/usr/bin/env python

import sys
import re

regex = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

total = 0

for match in regex.finditer(sys.stdin.read()):
    a, b = map(int, match.groups())
    total += a * b

print(total)
