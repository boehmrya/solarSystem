
import math


class Planet:
	def __init__(self, iname, irad, im, idist, inumMoons, imoonList):
		self.name = iname
		self.radius = irad
		self.mass = im
		self.distance = idist
		self.numMoons = inumMoons
		self.moonList = imoonList

	# accessor methods
	def getName(self):
		return self.name

	def getRadius(self):
		return self.radius

	def getMass(self):
		return self.mass

	def getDistance(self):
		return self.distance

	def getNumMoons(self):
		return self.numMoons

	def getCircumference(self):
		c = math.pi * (2 * self.radius)
		return c

	def getVolume(self):
		v = 4/3 * math.pi * self.radius**3
		return v

	def getSurfaceArea(self):
		sa = 4 * math.pi * self.radius**2
		return sa

	def getDensity(self):
		d = self.mass / self.getVolume()
		return d

	# mutator methods
	def setName(self, newName):
		self.name = newName

	def setNumMoons(self, newNumMoons):
		self.numMoons = newNumMoons

	def addMoon(self, moonName):
		self.moonList.append(moonName)

	# to string method
	def __str__(self):
		return self.name





myPlanet = Planet("X25", 45, 198, 1000, 3)
print(myPlanet.getName())
myPlanet.setName('Hydra')
print(myPlanet.getName())








