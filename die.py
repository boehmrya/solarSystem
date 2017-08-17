

import random


class Die:
	def __init__(self, inumSides):
		self.numSides = inumSides

	def roll(self):
		result = random.randint(1, self.numSides)
		return result

	# to string method
	def __str__(self):
		name = str(self.numSides) + " sided die"
		return name

	def __ge__(self, other):
		return self.roll() >= other.roll()

	def __gt__(self, other):
		return self.roll() > other.roll()

	def __le__(self, other):
		return self.roll() <= other.roll()

	def __lt__(self, other):
		return self.roll() < other.roll()

	def __eq__(self, other):
		return self.roll() == other.roll()

	def __ne__(self, other):
		return self.roll() != other.roll()


myDie = Die(6)
otherDie = Die(6)
print(myDie.__ge__(otherDie))






