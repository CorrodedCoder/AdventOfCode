# AdventOfCode

See https://adventofcode.com/2022/day/4

Hard to polish this one. Three areas:
1) Deserialize string data to numbers. Only really liked the regex but it was way slower than the simplest approach.
2) I think the check for if either range is entirely contained within the other could be done with less checks. Maybe.

For each part I chose:
* A plain all written in one function approach because it was the fastest.
* A regex variant of the fastest to demonstrate sadly how much slower the regex one was.
* An alternate variant aiming to be cleaner to make sense of but is a bit slower than the fastest.
* A second alternate variant which is ever so slightly faster than the fastest :^\.

To get some performance statistics:
* python -m timeit -s "from solution_part1_plain import solve" "solve(open('input.txt'))"
* python -m timeit -s "from solution_part1_regex import solve" "solve(open('input.txt'))"
* python -m timeit -s "from solution_part1_alt import solve" "solve(open('input.txt'))"
* python -m timeit -s "from solution_part1_alt2 import solve" "solve(open('input.txt'))"
* python -m timeit -s "from solution_part2_plain import solve" "solve(open('input.txt'))"
* python -m timeit -s "from solution_part2_regex import solve" "solve(open('input.txt'))"
* python -m timeit -s "from solution_part2_alt import solve" "solve(open('input.txt'))"

Works fine with latest python 2 and 3.
