# AdventOfCode

See https://adventofcode.com/2022/day/1

For each part I chose:
* One approach where I leveraged as much of the python libraries as I could think of to solve the problem
* One approach which laid it out as clearly as I could think of.

In both cases I had an eye towards performance and memory use.

To get some performance statistics:
* python -m timeit -s "from solution_part1_leverage import sum_largest" "sum_largest(open('input.txt'))"
* python -m timeit -s "from solution_part1_cleaner import sum_largest" "sum_largest(open('input.txt'))"
* python -m timeit -s "from solution_part2_leverage import sum_three_largest" "sum_three_largest(open('input.txt'))"
* python -m timeit -s "from solution_part2_cleaner import sum_three_largest" "sum_three_largest(open('input.txt'))"

In my observations the cleaner variant was about 1.5 times faster than the library oriented one.

Works fine with latest python 2 and 3.
