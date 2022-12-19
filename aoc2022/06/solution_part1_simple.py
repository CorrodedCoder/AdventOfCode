def find_marker(sequence):
    for index in range(len(sequence) - 4):
        if len(set(sequence[index:index+4])) == 4:
            return index + 4

def solve(sequence):
    return find_marker(sequence)

if __name__ == '__main__':
    import sys
    print(solve(open(sys.argv[1]).readline()))
