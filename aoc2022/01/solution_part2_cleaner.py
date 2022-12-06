import heapq

# Notes:
# * Used generator for clarity.
# * Seems fastest approach I tried and should use least memory.

def sum_groups(iterable):
	total = 0
	for line in iterable:
		if line == '\n':
			yield total
			total = 0
		else:
			total += int(line)
	if total > 0:
		yield total

def sum_three_largest(iterable):
	# Three element heap
	heap = [0,0,0]

	for total in sum_groups(iterable):
		# Push the new element and pop the lowest/smallest value
		heapq.heappushpop(heap, total)

	return sum(heap)

if __name__ == '__main__':
	import sys
	print(sum_three_largest(open(sys.argv[1])))
