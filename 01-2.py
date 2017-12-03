#!/usr/bin/env python3

import sys

puzzle = sys.argv[1]
prev = None
total = 0
puzzle_half = len(puzzle)//2
to_match = puzzle_half

for idx, num  in enumerate(puzzle):
    num = int(num)
    if to_match >= len(puzzle):
        to_match *= -1
    if num == int(puzzle[to_match]):
        total += num
    to_match += 1

print(total)

