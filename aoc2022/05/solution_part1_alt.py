import itertools

def solve(iterable):
    # Read each row of the crates until we get a newline
    crate_rows = (line[1::4] for line in itertools.takewhile(lambda x: x != '\n', iterable))
    # Generate the stacks from the rows, removing any spaces from the top
    stacks = [list(reversed(list(itertools.dropwhile(lambda x: x == ' ', stack)))) for stack in zip(*crate_rows)]
    for move_str in iterable:
        _, count_str, _, source_str, _, destination_str = move_str.split(' ')
        # source and destination need a -1 for zero based indexing
        count, source, destination = int(count_str), int(source_str) - 1, int(destination_str) - 1
        # Build new stack from reversed "count" top of source + current stack
        stacks[destination].extend(stacks[source][:-count-1:-1])
        # Remove "count" top of source from current stack
        del stacks[source][-count:]
    return ''.join(stack[-1] for stack in stacks)
        

if __name__ == '__main__':
    import sys
    print(solve(open(sys.argv[1])))
