

class solarSystem:
	def __init__(self, asun):
		self.thesun = asun
		self.planets = []

	def addPlanet(self, aplanet):
		self.planets.append(aplanet)

	def showPlanets(self):
		for aplanet in self.planets:
			print(aplanet)





