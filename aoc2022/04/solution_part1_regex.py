import re

_regex_match = re.compile(r'(\d+)-(\d+),(\d+)-(\d+)\n')

def solve(iterable):
    count = 0
    for row in iterable:
        s1, e1, s2, e2 = re.match(_regex_match, row).groups()
        if (int(s1) >= int(s2) and int(e1) <= int(e2)) or (int(s2) >= int(s1) and int(e2) <= int(e1)):
            count += 1
    return count

if __name__ == '__main__':
    import sys
    print(solve(open(sys.argv[1])))
