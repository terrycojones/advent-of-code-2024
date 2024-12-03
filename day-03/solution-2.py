#!/usr/bin/env python

import sys
import re

regex = re.compile(r"(do|don't|mul)\((\d{1,3},\d{1,3})?\)")

total = 0
enabled = True

for match in regex.finditer(sys.stdin.read()):
    what, args = match.groups()
    if what == "do":
        enabled = True
    elif what == "don't":
        enabled = False
    else:
        if enabled:
            a, b = map(int, args.split(","))
            total += a * b

print(total)
