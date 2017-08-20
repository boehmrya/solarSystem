

class Fraction:
	def __init__(self, inum, idenom):
		self.num = inum
		self.denom = idemon	
		self.reduceTerms()


	@staticmethod
	def lowestComDenom(denom1, denom2):
		if denom1 == denom2:
			return denom1
		else:
			origDenom1 = denom1
			origDenom2 = denom2
			while denom1 != denom2:
				if denom1 < denom2:
					denom1 += origDenom1
				else:
					denom2 += origDenom2
			return denom1


	def convertNumDenom(self, newDenom):
		factor = newDenom / self.denom
		self.num = self.num * factor
		self.denom = newDenom


	def reduceTerms(self):
		if self.num <= self.denom:
			lowest = self.num
		else:
			lowest = self.denom
		while lowest > 0:
			if ((self.num % lowest == 0) && (self.denom % lowest == 0)):
				self.num = self.num / lowest
				self.denom = self.denom / lowest
				lowest = lowest / lowest
			else:
				lowest -= 1


	def __add__(self, other):
		lcd = lowestComDenom(self.denom, other.denom)
		self.convertNumDenom(lcd)
		other.convertNumDenom(lcd)
		self.num = self.num + other.num
		self.reduceTerms()
		

	def __sub__(self, other):
		lcd = lowestComDenom(self.denom, other.denom)
		self.convertNumDenom(lcd)
		other.convertNumDenom(lcd)
		self.num = self.num - other.num
		self.reduceTerms()
		

	def __mul__(self, other):
		self.num = self.num * other.num
		self.denom = self.denom * other.denom


	def __truediv__(self, other):
		# flip and multiply
		self.num = self.denom * other.num
		self.denom = self.num * other.denom


	def __ge__(self, other):
		lcd = lowestComDenom(self.denom, other.denom)
		self.convertNumDenom(lcd)
		other.convertNumDenom(lcd)
		if self.num >= other.num:
			return true
		else:
			return false


	def __gt__(self, other):
		lcd = lowestComDenom(self.denom, other.denom)
		self.convertNumDenom(lcd)
		other.convertNumDenom(lcd)
		if self.num > other.num:
			return true
		else:
			return false


	def __le__(self, other):
		lcd = lowestComDenom(self.denom, other.denom)
		self.convertNumDenom(lcd)
		other.convertNumDenom(lcd)
		if self.num <= other.num:
			return true
		else:
			return false


	def __lt__(self, other):
		lcd = lowestComDenom(self.denom, other.denom)
		self.convertNumDenom(lcd)
		other.convertNumDenom(lcd)
		if self.num < other.num:
			return true
		else:
			return false


	def __eq__(self, other):
		lcd = lowestComDenom(self.denom, other.denom)
		self.convertNumDenom(lcd)
		other.convertNumDenom(lcd)
		if self.num == other.num:
			return true
		else:
			return false


	def __ne__(self, other):
		lcd = lowestComDenom(self.denom, other.denom)
		self.convertNumDenom(lcd)
		other.convertNumDenom(lcd)
		if self.num != other.num:
			return true
		else:
			return false


	def __str__(self):
		name = str(self.num) + " / " + str(self.denom)
		return name

	
