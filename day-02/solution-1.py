#!/usr/bin/env python

import sys
from utils import safe

print(sum(safe(list(map(int, line.split()))) for line in sys.stdin))
