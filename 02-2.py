#!/usr/bin/env python3

import sys
import os

with open(sys.argv[1]) as f:
    puzzle = f.readlines()

total = 0
for line in puzzle:
    row = [int(x) for x in line.split()]
    print(row)
    idx = 0
    while idx < len(row) - 1:
        num = row[idx]
        print(num, row[idx + 1], num % row[idx + 1], row[idx + 1] % num)
        idx += 1
    print("\n")

    total += max(row) - min(row)

print(total)
