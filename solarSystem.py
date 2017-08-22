
from sun import *
from planet import *
import turtle
import math

class SolarSystem:
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

	def movePlanets(self):
		G = .1
		dt = .001

		for p in self.planets:
			p.moveTo(p.getXPos() + dt * p.getXVel(),
					 p.getYPos() + dt * p.getYVel())

			rx = self.thesun.getXPos() - p.getXPos()
			ry = self.thesun.getYPos() - p.getYPos()
			r = math.sqrt(rx**2 + ry**2)

			accx = G * self.thesun.getMass() * (rx / r**3)
			accy = G * self.thesun.getMass() * (ry / r**3)

			p.setXVel(p.getXVel() + dt * accx)
			p.setYVel(p.getYVel() + dt * accy)

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



def createSSandAnimate():
	#create solar system
	ss = SolarSystem(2,2)

	# create and add sun
	sun = Sun("SUN", 5000, 10, 5800)
	ss.addSun(sun)

	# create and add planets
	m = Planet("MERCURY", 19.5, 1000, .25, 0, 2.0, "blue")
	ss.addPlanet(m)

	m = Planet("EARTH", 47.5, 5000, .3, 0, 2.0, "green")
	ss.addPlanet(m)

	m = Planet("MARS", 50, 9000, .5, 0, 1.63, "red")
	ss.addPlanet(m)

	m = Planet("JUPITER", 100, 49000, .7, 0, 1, "black")
	ss.addPlanet(m)

	numTimePeriods = 2000
	for amove in range(numTimePeriods):
		ss.movePlanets()

	ss.freeze()


createSSandAnimate()







