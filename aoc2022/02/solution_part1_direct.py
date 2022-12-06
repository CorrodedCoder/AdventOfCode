from solution_common import *

_opponent_char_to_shape = {
	'A': Shapes.Rock,
	'B': Shapes.Paper,
	'C': Shapes.Scissors,
}

_suggested_char_to_shape = {
	'X': Shapes.Rock,
	'Y': Shapes.Paper,
	'Z': Shapes.Scissors,
}

def opponent_char_to_shape(c):
	return _opponent_char_to_shape[c]

def suggested_char_to_shape(c):
	return _suggested_char_to_shape[c]

def read_hints(iterable):
	for line in iterable:
		(opponent,_,suggested,_) = line
		yield (opponent_char_to_shape(opponent), suggested_char_to_shape(suggested))

_round_score = {(opponent, shape): shape + result for opponent, shape, result in truth_table}

def tournament(iterable):
	return sum(_round_score[(opponent, suggested)] for opponent, suggested in read_hints(iterable))

if __name__ == '__main__':
	import sys
	print(tournament(open(sys.argv[1])))
