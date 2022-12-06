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

_outcome_score = {(opponent, shape): result for opponent, shape, result in truth_table}

def outcome_score(opponent, suggested):
	return _outcome_score[(opponent, suggested)]

def round_score(opponent, shape):
	return shape + outcome_score(opponent, shape)

_intended_outcome = {(shapes[0], result): shapes[1] for shapes, result in _outcome_score.items()}

def shape_for_result(opponent, intended_result):
	return _intended_outcome[(opponent, intended_result)]

def tournament(iterable):
	return sum(round_score(opponent, shape_for_result(opponent, intended_result)) for opponent, intended_result in read_hints(iterable))

if __name__ == '__main__':
	import sys
	print(tournament(open(sys.argv[1])))
