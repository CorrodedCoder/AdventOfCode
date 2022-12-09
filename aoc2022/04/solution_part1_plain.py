
def solve(iterable):
    count = 0
    for row in iterable:
        seq1, seq2 = row[:-1].split(',')
        s1, e1 = seq1.split('-')
        s2, e2 = seq2.split('-')
        if (int(s1) >= int(s2) and int(e1) <= int(e2)) or (int(s2) >= int(s1) and int(e2) <= int(e1)):
            count += 1
    return count

if __name__ == '__main__':
    import sys
    print(solve(open(sys.argv[1])))
