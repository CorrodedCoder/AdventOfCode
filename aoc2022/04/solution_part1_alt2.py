
def decode_row(iterable):
    for row in iterable:
        seq1, seq2 = row[:-1].split(',')
        s1, e1 = seq1.split('-')
        s2, e2 = seq2.split('-')
        yield int(s1), int(e1), int(s2), int(e2)


def solve(iterable):
    return sum(1 for s1, e1, s2, e2 in decode_row(iterable) if (s1 >= s2 and e1 <= e2) or (s2 >= s1 and e2 <= e1))

if __name__ == '__main__':
    import sys
    print(solve(open(sys.argv[1])))
