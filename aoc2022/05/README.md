# AdventOfCode

See https://adventofcode.com/2022/day/5

Three versions of each:
1) Simple: Just a simple straightforward train of thought. Uses a list like a stack where the top gets moved from the top of one stack to another.
2) Regex: Same as simple, but uses regex for deserialising input. Much slower.
3) Alt: A list like an upside down stack where things are moved from the end of one to the end of another. I thought it would have been faster than the simple one as it was just working at the end of a list, but I could measure no difference.

Only one line differs between first and second solution, so I guess I could have made it common and passed in a lambda for the different behaviour.

Not very self documenting code because I didn't feel like it, so I added some comments at least to indicate what I was doing. It's not my finest work.

I also experimented with:
 1) modifying it in place: insert at the start - I checked this, it seemed slower - possibly because inserting was multiple insert calls.
 2) using an array: tried it, made no difference.
 3) using a deque: tried it, it seemed slower - possibly because removal was multiple popleft calls.

To get some performance statistics:
* python -m timeit -s "from solution_part1_simple import solve" "solve(open('input.txt'))"
* python -m timeit -s "from solution_part1_regex import solve" "solve(open('input.txt'))"
* python -m timeit -s "from solution_part1_alt import solve" "solve(open('input.txt'))"
* python -m timeit -s "from solution_part2_simple import solve" "solve(open('input.txt'))"
* python -m timeit -s "from solution_part2_regex import solve" "solve(open('input.txt'))"
* python -m timeit -s "from solution_part2_alt import solve" "solve(open('input.txt'))"

Works fine with latest python 2 and 3.
