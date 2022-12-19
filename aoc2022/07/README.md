# AdventOfCode

See https://adventofcode.com/2022/day/7

My main focus here was to provide a generator to walk the directories such that the calling code did not need to maintain a list of directories if there was no need i.e. part 1, but to avoid walking the directories twice for part 2
I used a list anyway.

The function used for parsing the input is identical for part 1 and part 2 so I factored that into solution_common.py

Two versions here:
1) Iterative: it looks ugly, although should be relatively efficient.
2) Recursive: it... well... it still looks quite ugly, and is less efficient than the iterative approach.

To get some performance statistics:
* python -m timeit -s "from solution_part1_iterative import solve" "solve(open('input.txt'))"
* python -m timeit -s "from solution_part1_recursive import solve" "solve(open('input.txt'))"
* python -m timeit -s "from solution_part2_iterative import solve" "solve(open('input.txt'))"
* python -m timeit -s "from solution_part2_recursive import solve" "solve(open('input.txt'))"

Works fine with latest python 2 and 3.
