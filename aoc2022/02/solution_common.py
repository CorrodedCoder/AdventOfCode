import sys

if sys.hexversion >= 0x03040000:
	from enum import IntEnum as MyIntEnum
else:
	# Compatibility tweak for Python 2, although we get very little of the benefits and many drawbacks
	MyIntEnum = object


class Shapes(MyIntEnum):
	Rock = 1
	Paper = 2
	Scissors = 3

class Results(MyIntEnum):
	Win = 6
	Draw = 3
	Lose = 0

truth_table = (
	(Shapes.Rock, Shapes.Rock, Results.Draw),
	(Shapes.Rock, Shapes.Paper, Results.Win),
	(Shapes.Rock, Shapes.Scissors, Results.Lose),
	(Shapes.Paper, Shapes.Rock, Results.Lose),
	(Shapes.Paper, Shapes.Paper, Results.Draw),
	(Shapes.Paper, Shapes.Scissors, Results.Win),
	(Shapes.Scissors, Shapes.Rock, Results.Win),
	(Shapes.Scissors, Shapes.Paper, Results.Lose),
	(Shapes.Scissors, Shapes.Scissors, Results.Draw),
	)
