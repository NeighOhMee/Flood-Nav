'''
this file contains the grid class that is in charge of holding the data for the rows
'''

class grid(object):
	def __init__(self, Fconnections, bound1, bound2):
		#vector that holds all the data
		self.floodCon = set()
		self.path = set()
		self.bound = bound1, bound2
		for ls in Fconnections:
			tup1 = ls[0], ls[1]
			tup2 = ls[2], ls[3]
			if tup1 < tup2:
				setString = str(ls[0]) + str(ls[1]) + str(ls[2]) + str(ls[3])
			else:
				setString = str(ls[2]) + str(ls[3]) + str(ls[0]) + str(ls[1])
			self.floodCon.add(setString)

	def checkConnection(self,point1, point2):
		#Checks if two points are connected, returns 0 if connected, 1 if flooded, 2 if out 
		#of range 
		if point1 < self.bound[0] or point1 > self.bound[1] or point2< self.bound[0] or point2 > self.bound[1]:
			return 2
		if point1 < point2:
			setString = str(point1[0]) + str(point1[1]) + str(point2[0]) + str(point2[1])
		else:
			setString = str(point2[0]) + str(point2[1]) + str(point1[0]) + str(point1[1])
		if setString in self.floodCon:
			return 1
		if setString in self.path:
			return 3
		return 0

	def addFlooded(self, point1, point2):
		if point1 < point2:
			setString = str(point1[0]) + str(point1[1]) + str(point2[0]) + str(point2[1])
		else:
			setString = str(point2[0]) + str(point2[1]) + str(point1[0]) + str(point1[1])
		if setString not in self.floodCon:
			self.floodCon.add(setString)

	def addPath(self, point1, point2):
		if point1 < point2:
			setString = str(point1[0]) + str(point1[1]) + str(point2[0]) + str(point2[1])
		else:
			setString = str(point2[0]) + str(point2[1]) + str(point1[0]) + str(point1[1])
		if setString not in self.path:
			self.path.add(setString)

	def removeFlooded(self, point1, point2):
		if point1 < point2:
			setString = str(point1[0]) + str(point1[1]) + str(point2[0]) + str(point2[1])
		else:
			setString = str(point2[0]) + str(point2[1]) + str(point1[0]) + str(point1[1])
		if setString not in self.floodCon:
			self.floodCon.remove(setString)
	'''
	def addPerson(self, point1, point2):
		#adds a person to the list of 
	'''
		


if __name__ == "__main__":
	test = grid([(1,0,2,0),(1,0,1,1),(1,1,2,1),(0,2,1,2)], (0,0), (32,32))
	print(test.checkConnection((1,0),(1,-1)))
	print(test.checkConnection((1,1),(1,0)))
	print(test.checkConnection((1,1),(2,1)))
	print(test.checkConnection((0,2),(1,2)))
	print(test.checkConnection((0,0),(6,8)))
	print(test.checkConnection((0,0), (-1,-1)))
	print(test.checkConnection((0,0), (35,35)))
