import itertools

# Notes:
# * Leverages as many of the library approaches as I can think of.
# * Intentional one liner - not aiming for readabity :/
# * Aiming for efficient use of memory and performance by using generators throughout.

def sum_largest(iterable):
	return max(sum(int(numstr) for numstr in value) for key, value in itertools.groupby(iterable, lambda x: x == '\n') if not key)

if __name__ == '__main__':
	import sys
	print(sum_largest(open(sys.argv[1])))
