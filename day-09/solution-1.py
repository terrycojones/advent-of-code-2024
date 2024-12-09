#!/usr/bin/env python

import sys


def readData():
    data = []
    free = False
    for i, length in enumerate(map(int, sys.stdin.read().strip())):
        file_id = None if free else i >> 1
        data.extend([file_id] * length)
        free = not free

    return data


data = readData()
last = len(data) - 1
first = checksum = 0

while True:
    while data[first] is not None:
        checksum += first * data[first]
        first += 1
    if first == last:
        break
    while data[last] is None:
        last -= 1

    data[first], data[last] = data[last], None

print(checksum)
