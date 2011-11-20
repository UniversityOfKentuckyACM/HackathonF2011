import util

class WorldLoader:
	north = {}
	south = {}
	east = {}
	west = {}
	def __init__(self, worldname):
		f = open("../data/maps/"+worldname, 'r')
		lines = f.readlines()
		for line in lines:
			args = line.split()
			self.north[args[0]] = args[1] 
			self.south[args[0]] = args[2] 
			self.east[args[0]] = args[3] 
			self.west[args[0]] = args[4] 
