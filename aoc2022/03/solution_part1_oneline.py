import string

def solve(input):
    return sum(string.ascii_letters.index(list(set(contents[:len(contents)//2]) & set(contents[len(contents)//2:]))[0]) + 1 for contents in input)

if __name__ == '__main__':
    import sys
    print(solve(open(sys.argv[1])))
