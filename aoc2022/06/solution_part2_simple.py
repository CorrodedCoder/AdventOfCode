def find_marker(sequence, size):
    for index in range(len(sequence) - size):
        if len(set(sequence[index:index+size])) == size:
            return index + size

def solve(sequence):
    return find_marker(sequence, 14)

if __name__ == '__main__':
    import sys
    print(solve(open(sys.argv[1]).readline()))
