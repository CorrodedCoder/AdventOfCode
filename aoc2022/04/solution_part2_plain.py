
def solve(iterable):
    count = 0
    for row in iterable:
        seq1, seq2 = row[:-1].split(',')
        s1, e1 = seq1.split('-')
        s2, e2 = seq2.split('-')
        if int(e1) >= int(s2) and int(e2) >= int(s1):
            count += 1
    return count

if __name__ == '__main__':
    import sys
    print(solve(open(sys.argv[1])))
