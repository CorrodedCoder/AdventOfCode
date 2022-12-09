
def does_range_overlap(row):
    seq1, seq2 = row[:-1].split(',')
    s1, e1 = seq1.split('-')
    s2, e2 = seq2.split('-')
    return int(e1) >= int(s2) and int(e2) >= int(s1)

def solve(iterable):
    return sum(does_range_overlap(row) for row in iterable)

if __name__ == '__main__':
    import sys
    print(solve(open(sys.argv[1])))
