import sys

if sys.version_info.major == 2:
	# Compatibility tweak for Python 2, although we get very little of the benefits and many drawbacks
	MyEnumClass = object
else:
	from enum import IntEnum
	MyEnumClass = IntEnum

class Shapes(MyEnumClass):
	Rock = 1
	Paper = 2
	Scissors = 3

class Results(MyEnumClass):
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
