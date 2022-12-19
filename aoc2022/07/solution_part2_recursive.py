from solution_common import parse_directory_recursive


def solve(iterable):
    capacity = 70000000
    required_unused = 30000000
    dir_sizes = list(parse_directory_recursive(iterable))
    used = dir_sizes[-1][1]
    # Assumes that a directory actually needs to be deleted
    remaining_size_needed = required_unused - (capacity - used)
    return min(size for _, size in dir_sizes if size >= remaining_size_needed)


if __name__ == '__main__':
    import sys
    print(solve(open(sys.argv[1])))
