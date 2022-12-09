
def is_range_contained(row):
    seq1, seq2 = row[:-1].split(',')
    s1, e1 = seq1.split('-')
    s2, e2 = seq2.split('-')
    return (int(s1) >= int(s2) and int(e1) <= int(e2)) or (int(s2) >= int(s1) and int(e2) <= int(e1))

def solve(iterable):
    return sum(is_range_contained(row) for row in iterable)

if __name__ == '__main__':
    import sys
    print(solve(open(sys.argv[1])))
