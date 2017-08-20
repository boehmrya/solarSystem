
import math

class Sun:
	def __init__(self, iname, irad, im, itemp):
		self.name = iname
		self.radius = irad
		self.mass = im
		self.temp = itemp

	def getMass(self):
		return self.mass

	def getRadius(self):
		return self.radius

	def getTemperature(self):
		return self.temp

	def getVolume(self):
		v = 4/3 * math.pi * self.radius**3
		return v

	def getSurfaceArea(self):
		sa = 4 * math.pi * self.radius**2
		return sa

	def getDensity(self):
		d = self.mass / self.getVolume()
		return d

	def setName(self, newName):
		self.name = newName

	def setRadius(self, newRadius):
		self.radius = newRadius

	def printTable(self):
		# print table header
		print("radius " + "volume " + " surface area")
		oldRadius = self.radius
		# reset value to 10, will reset to old value later
		testRadius = 10
		while testRadius <= 500:
			self.setRadius(testRadius)
			print(self.getRadius() + " " + self.getVolume() + " " + self.getSurfaceArea())
			testRadius += 10

	def __str__(self):
		return self.name