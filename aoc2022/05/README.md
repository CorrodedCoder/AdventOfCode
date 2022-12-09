# AdventOfCode

See https://adventofcode.com/2022/day/5

Just a simple straightforward train of thought version for now. Not feeling like polishing this bad boy for performance just yet.

Only one line differs between first and second solution, so I guess I could have made it common and passed in a lambda for the different behaviour.

Not very self documenting code because I didn't feel like it, so I added some comments at least to indicate what I was doing. It's not my finest work.

Feel like aside from the obvious optimisation of the regex, I wonder at the data structure I use (a list) and how I use it (overwriting the old with a newly constructed list) could be improved by:
 1) modifying it in place: insert at the start - I checked this, it seemed slower.
 2) using an array: tried it, made no difference.
 3) working on the list in reverse order, so we're only ever adding/removing from the end
 4) using a deque

To get some performance statistics:
* python -m timeit -s "from solution_part1_simple import solve" "solve(open('input.txt'))"
* python -m timeit -s "from solution_part2_simple import solve" "solve(open('input.txt'))"

Works fine with latest python 2 and 3.
