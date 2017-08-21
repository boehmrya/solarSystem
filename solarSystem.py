
from sun import *
from planet import *
import turtle

class solarSystem:
	def __init__(self, width, height):
		self.thesun = None
		self.planets = []
		#turtle object
		self.ssturtle = turtle.Turtle()
		self.ssturtle.hideturtle()
		self.ssscreen = turtle.Screen()
		self.ssscreen.setworldcoordinates( -width / 2.0, -height / 2.0, width / 2.0, height / 2.0 )

	def addPlanet(self, aplanet):
		self.planets.append(aplanet)

	def addSun(self, asun):
		self.thesun = asun

	# print out list of planets
	def showPlanets(self):
		for aplanet in self.planets:
			print(aplanet)

	def freeze(self):
		self.ssscreen.exitonclick()

	# total number of planets in the solar system
	def numPlanets(self):
		return len(self.planets)

	# total mass of all planets, including the sun
	def totalMass(self):
		totalMass = self.thesun.getMass()
		for planet in self.planets:
			totalMass += planet.getMass()
		return totalMass

	def removePlanet(self, aplanet):
		self.planets.remove(aplanet)

	# get the closest planet to the sun (in terms of distance)
	def getNearest(self):
		# set min to first item
		minDist = planets[0].getDistance() 
		minDistPlanet = planets[0]
		# determine the planet with shortest distance
		for planet in planets:
			if planet.getDistance() < minDist:
				minDist = planet.getDistance()
				minDistPlanet = planet
		return minDistPlanet

	# get the farthest planet away from the sun (in terms of distance)
	def getFarthest(self):
		# set max to first item
		maxDist = planets[0].getDistance() 
		maxDistPlanet = planets[0]
		# determine the planet with farthest distance
		for planet in planets:
			if planet.getDistance() > maxDist:
				maxDist = planet.getDistance()
				maxDistPlanet = planet
		return maxDistPlanet

	# to string method for printing
	def __str__(self):
		planetList = [self.thesun]
		tempPlanets = self.planets #to restore after method
		while len(self.planets) > 0:
			closest = self.getNearest()
			planetString.append(closest)
			self.remove(closest)
		# restore planets list on object
		self.planets = tempPlanets
		# print planets in new ordered list
		for planet in planetList:
			print(planet)






mySun = Sun("theSun", 10, 45, 3)
print(mySun)







