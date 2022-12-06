# AdventOfCode

See https://adventofcode.com/2022/day/2

For each part I chose:
* One approach where I laid it out in a hopefully understandable way (pedestrian)
* One approach which I simplified the processing into a single table lookup with an eye towards performance.

To get some performance statistics:
* python -m timeit -s "from solution_part1_pedestrian import tournament" "tournament(open('input.txt'))"
* python -m timeit -s "from solution_part1_direct import tournament" "tournament(open('input.txt'))"
* python -m timeit -s "from solution_part2_pedestrian import tournament" "tournament(open('input.txt'))"
* python -m timeit -s "from solution_part2_direct import tournament" "tournament(open('input.txt'))"

In my observations the direct variant were about 1.25 and 1.5 times faster respectively than the pedestrian ones.

Works fine with latest python 2 and 3 (because of a dodgy workaround in solution_common.py).
