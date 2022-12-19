# AdventOfCode

See https://adventofcode.com/2022/day/6

Not much to say about this one. Only one solution for each. The first solution could be reworked to call the same function as the second solution, but it didn't seem worth it this time as it's more of a code fragment.

To get some performance statistics:
* python -m timeit -s "from solution_part1_simple import solve" "solve(open('input.txt'))"
* python -m timeit -s "from solution_part2_simple import solve" "solve(open('input.txt'))"

Works fine with latest python 2 and 3.
