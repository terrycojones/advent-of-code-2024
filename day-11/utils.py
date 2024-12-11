import sys
from functools import cache


def getData():
    stones = tuple(map(int, sys.stdin.read().split()))
    iterations = int(sys.argv[1])
    return stones, iterations


@cache
def blink1(stone):
    if stone == 0:
        return (1,)
    elif (length := len(str(stone))) % 2 == 0:
        ss = str(stone)
        n = length >> 1
        return int(ss[:n]), int(ss[n:])
    else:
        return (stone * 2024,)
