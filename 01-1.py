#!/usr/bin/env python3

import sys

puzzle = sys.argv[1]

prev = None
total = 0
for i in puzzle:
    if prev == i:
        total += int(i)
    prev = i

if puzzle[-1] == puzzle[0]:
    total += int(i)

print(total)

