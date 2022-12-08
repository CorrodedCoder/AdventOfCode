import string

def solve(input):
    return sum(string.ascii_letters.index(list((set(a[:-1]) & set(b[:-1]) & set(c[:-1])))[0]) + 1 for a,b,c in zip(*([iter(input)] * 3)))

if __name__ == '__main__':
    import sys
    print(solve(open(sys.argv[1])))
