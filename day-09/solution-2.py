#!/usr/bin/env python

import sys
from dataclasses import dataclass


@dataclass
class Node:
    free: bool
    file_id: int
    length: int
    next_: "Node"
    prev: "Node"


def readData():
    free = False
    head = tail = None
    for i, length in enumerate(map(int, sys.stdin.read().strip())):
        if length:
            new = Node(free, None if free else i >> 1, length, None, tail)
            if tail:
                tail.next_ = new
            else:
                assert head is None
                head = new
            tail = new
        free = not free

    return head, tail


head, tail = readData()

first_free = head
while not first_free.free:
    first_free = first_free.next_

last_file = tail
while last_file.free:
    last_file = last_file.prev


while last_file is not head:
    previous_file = last_file.prev
    while previous_file and previous_file.free:
        previous_file = previous_file.prev

    split_candidate = first_free
    while split_candidate:
        if split_candidate is last_file:
            split_candidate = None
            break
        if split_candidate.free and split_candidate.length >= last_file.length:
            break
        split_candidate = split_candidate.next_

    if split_candidate:
        split_candidate.free = False
        split_candidate.file_id = last_file.file_id
        extra = split_candidate.length - last_file.length
        split_candidate.length = last_file.length

        if extra > 0:
            new = Node(True, None, extra, split_candidate.next_, split_candidate)
            split_candidate.next_.prev = new
            split_candidate.next_ = new

        last_file.file_id = None
        last_file.free = True

    last_file = previous_file


checksum = 0
node = head
block = 0

while node:
    if not node.free:
        for i in range(node.length):
            checksum += node.file_id * (block + i)

    block += node.length
    node = node.next_


print(checksum)
