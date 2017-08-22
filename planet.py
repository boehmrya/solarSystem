
import math
import turtle

class Planet:
	def __init__(self, iname, irad, im, ivx, ivy, idist, ic):
		self.name = iname
		self.radius = irad
		self.mass = im
		self.distance = idist
		self.x = idist
		self.y = 0
		self.ivx = ivx
		self.ivy = ivy
		self.color = ic
		#turtle object
		self.pturtle = turtle.Turtle()
		self.pturtle.color(self.color)
		self.pturtle.shape("circle")
		self.pturtle.up()
		self.pturtle.goto(self.x, self.y)
		self.pturtle.down()
		self.pturtle.resizemode("user")	
		self.pturtle.shapesize(0.006 * self.radius, 0.006 * self.radius)

	def getXPos(self):
		return self.x

	def getYPos(self):
		return self.y

	def getName(self):
		return self.name

	def getRadius(self):
		return self.radius

	def getMass(self):
		return self.mass

	def getXVel(self):
		return self.velx

	def getYVel(self):
		return self.vely

	# distance from sun
	def getDistance(self):
		return self.distance

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

	def moveTo(self, newx, newy):
		self.x = newx
		self.y = newy
		self.pturtle.goto(newx, newy)

	def setXVel(self, newvx):
		self.velx = newvx

	def setYVel(self, newvy):
		self.vely = newvy

	def setName(self, newName):
		self.name = newName

	# to string method
	def __str__(self):
		return self.name








