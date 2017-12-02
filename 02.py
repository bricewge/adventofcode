#!/usr/bin/env python3

import sys
import os

with open(sys.argv[1]) as f:
    puzzle = f.readlines()
print(puzzle)

total = 0
for line in puzzle:
    print(line)
    total += int(max(line.split())) - int(min(line.split()))
print(total)
