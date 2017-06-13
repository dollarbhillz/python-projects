#Incomplete - check blackboard for full code

def readPuzzle(fileName):
	"""Read a sudoku puzzle from a file
	
	Parameter: fileName - the name of the file
	Returns: internal representation of the puzzle
	"""
	file = open(fileName)
	
	
def printPuzzle(puzzle):
	""" """
	
def findSolution(puzzle):
	"""Solve a sudoku puzzle
	
	   Parameter: puzzle - the puzzle to solve - will be changed into (partial) solution
	   Returns: True if a solution was found; False if only a partial solution was found
	"""
	
	filledIn = countFilledIn(puzzle)
	setPossibilities(puzzle)
	while filledIn < 81:
		forced = findForcedCell(puzzle)
		if forced == None:
			return False
		fillInForced(forced, puzzle)
		excludeFromNeighbors(forced, puzzle)
		filledIn += 1
	return True
		
def countFilledIn(puzzle):
	"""Set each cell in a puzzle that is not yet filled in to a list of poss
	"""
	
def findForcedCell(puzzle):
	"""Find a cell in a puzzle that is not yet filled in, but for which there is only
	   one 
	   """
	   
def fillInForced(forced, puzzle):

def excludeFromNeighbors(cell, puzzle):
	"""Exclude a value from the possibilities for all neighbors
	"""