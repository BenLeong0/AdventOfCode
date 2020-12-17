cubes1 = {}
cubes2 = {} 
cycleLimit = 6

with open("inputs/day17input", 'r') as f:
	i = 0
	line = f.readline()
	size = len(line) - 1
	while line:
		j = 0
		while j < size:
			cubes1[(i,j,0)] = line[j]
			cubes2[(i,j,0,0)] = line[j]
			j += 1
		i += 1
		line = f.readline()



def partOne(cubes=cubes1, cycle=1):
	def getNeighbours(x,y,z):
		result = []
		for i in range(-1,2):
			for j in range(-1,2):
				for k in range(-1,2):
					if i == j == k == 0:
						continue
					result.append((x+i,y+j,z+k))
		return result
	
	# Add new sides
	for x in range(-cycle-1, size+cycle+1):
		for y in range(-cycle-1, size+cycle+1):
			for z in range(-cycle-1, size+cycle+1):
				cube = (x,y,z)
				if cube not in cubes:
					cubes[cube] = '.'
	
	newCubes = {}
	for x in range(-cycle, size+cycle):
		for y in range(-cycle, size+cycle):
			for z in range(-cycle, size+cycle):
				cube = (x,y,z)
				activeNbrs = len([1 for p in getNeighbours(*cube) if cubes[p] == '#'])
				if cubes[cube] == '#':
					if activeNbrs in [2,3]:
						newCubes[cube] = '#'
					else:
						newCubes[cube] = '.'
				elif cubes[cube] == '.':
					if activeNbrs == 3:
						newCubes[cube] = '#'
					else:
						newCubes[cube] = '.'
					
	if cycle == cycleLimit:
		return print(list(newCubes.values()).count('#'))
	
	return partOne(newCubes, cycle+1)



def partTwo(cubes=cubes2, cycle=1):
	def getNeighbours(x,y,z,w):
		result = []
		for i in range(-1,2):
			for j in range(-1,2):
				for k in range(-1,2):
					for l in range(-1,2):
						if i == j == k == l == 0:
							continue
						result.append((x+i,y+j,z+k,w+l))
		return result
	
	# Add new sides
	for x in range(-cycle-1, size+cycle+1):
		for y in range(-cycle-1, size+cycle+1):
			for z in range(-cycle-1, size+cycle+1):
				for w in range(-cycle-1, size+cycle+1):
					cube = (x,y,z,w)
					if cube not in cubes:
						cubes[cube] = '.'
	
	newCubes = {}
	for x in range(-cycle, size+cycle):
		for y in range(-cycle, size+cycle):
			for z in range(-cycle, size+cycle):
				for w in range(-cycle, size+cycle):
					cube = (x,y,z,w)
					activeNbrs = len([1 for p in getNeighbours(*cube) if cubes[p] == '#'])
					if cubes[cube] == '#':
						if activeNbrs in [2,3]:
							newCubes[cube] = '#'
						else:
							newCubes[cube] = '.'
					elif cubes[cube] == '.':
						if activeNbrs == 3:
							newCubes[cube] = '#'
						else:
							newCubes[cube] = '.'
					
	if cycle == cycleLimit:
		return print(list(newCubes.values()).count('#'))
	
	return partTwo(newCubes, cycle+1)


#partOne()
partTwo()	
