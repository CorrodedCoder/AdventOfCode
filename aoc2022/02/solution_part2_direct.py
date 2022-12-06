from solution_common import *

_opponent_char_to_shape = {
	'A': Shapes.Rock,
	'B': Shapes.Paper,
	'C': Shapes.Scissors,
}

_intended_char_to_result = {
	'X': Results.Lose,
	'Y': Results.Draw,
	'Z': Results.Win,
}

def opponent_char_to_shape(c):
	return _opponent_char_to_shape[c]

def intended_char_to_result(c):
	return _intended_char_to_result[c]

def read_hints(iterable):
	for line in iterable:
		(opponent,_,intended_result,_) = line
		yield (opponent_char_to_shape(opponent), intended_char_to_result(intended_result))

_round_result = {(opponent, result): result + shape for opponent, shape, result in truth_table}

def tournament(iterable):
	return sum(_round_result[(opponent, intended_result)] for opponent, intended_result in read_hints(iterable))

if __name__ == '__main__':
	import sys
	print(tournament(open(sys.argv[1])))
