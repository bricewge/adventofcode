#!/usr/bin/env python3

import sys
import os

with open(sys.argv[1]) as f:
    puzzle = f.readlines()

total = 0
for line in puzzle:
    row = [int(x) for x in line.split()]
    total += max(row) - min(row)

print(total)
