from solution_common import parse_directory_iterative


def solve(iterable):
    return sum(size for _, size in parse_directory_iterative(iterable) if size <= 100000)


if __name__ == '__main__':
    import sys
    print(solve(open(sys.argv[1])))
