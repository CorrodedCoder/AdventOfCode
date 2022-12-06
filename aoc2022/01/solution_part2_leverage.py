import itertools
import heapq

# Notes:
# * Leverages as many of the library approaches as I can think of.
# * Intentional one liner in for loop - not aiming for readabity :/

def sum_three_largest(iterable):
	# Three element heap
	heap = [0,0,0]

	for total in (sum(int(numstr) for numstr in value) for key, value in itertools.groupby(iterable, lambda x: x == '\n') if not key):
		# Push the new element and pop the lowest/smallest value
		heapq.heappushpop(heap, total)

	return sum(heap)

if __name__ == '__main__':
	import sys
	print(sum_three_largest(open(sys.argv[1])))
