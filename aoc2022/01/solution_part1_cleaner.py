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

def sum_largest(iterable):
	return max(sum_groups(iterable))

if __name__ == '__main__':
	import sys
	print(sum_largest(open(sys.argv[1])))
