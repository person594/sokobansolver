import sys
import copy

def readLevel(f):
	level = []
	for line in f:
		row = []
		for ch in line:
			if ch != '\n':
				row.append(ch)
		level.append(row)
	return level

def printLevel(level):
	for row in level:
		s = ""
		for ch in row:
			s += ch
		print(s)



def findChar(char, level):
	r = 0
	for row in level:
		c = 0
		for ch in row:
			if ch == char: return (r, c)
			c+=1
		r += 1
	return None
		
def isClear(r, c, level) :
	if 0 <= r < len(level) and 0 <= c < len(level[r]):
		ch = level[r][c]
		return ch == '.' or ch == '·' or ch == '@' or ch == '<' or ch == '>'
	else: return False
	
def isBoulder(r, c, level):
	if 0 <= r < len(level) and 0 <= c < len(level[r]):
		return level[r][c] == '0'
	else: return False
	
def isWall(r, c, level):
	return not (isClear(r, c, level) or isBoulder(r, c, level))
	
def canTravel(r1, c1, r2, c2, level) :
	if not (isClear(r1, c1, level) and isClear(r2, c2, level)): return False
	if r1 == r2 and c1 == c2: return True
	#level2 = copy.deepcopy(level)
	oldChar = level[r1][c1]
	level[r1][c1] = 'X'
	ret = (canTravel(r1-1, c1, r2, c2, level) or canTravel(r1+1, c1, r2, c2, level)
		or canTravel(r1, c1-1, r2, c2, level) or canTravel(r1, c1+1, r2, c2, level))
	level[r1][c1] = oldChar
	return ret
		
def isStuck(r, c, level):
	if isClear(r, c, level): return False
	if not isBoulder(r, c, level): return True
	level[r][c] = 'X'
	stuck = ((isStuck(r-1, c, level) or isStuck(r+1, c, level)) and
	(isStuck(r, c-1, level) or isStuck(r, c+1, level)))
	level[r][c] = '0'
	return stuck

def listPositions(ch, level):
	l = []
	r = 0
	for row in level:
		c = 0
		for char in row:
			if char == ch: l.append((r, c))
			c += 1
		r += 1
	return l

def fill(r, c, char, level):
	if isClear(r, c, level) and level[r][c] != char:
		level[r][c] = char
		fill(r-1, c, char, level)
		fill(r+1, c, char, level)
		fill(r, c-1, char, level)
		fill(r, c+1, char, level)
		
def zone(r, c, level):
	level2 = copy.deepcopy(level)
	fill(r, c, 'X', level2)
	return findChar('X', level2)
	
def normalizePlayer(player, level):
	level[player[0]][player[1]] = '.'
	z = zone(player[0], player[1])
	level[z[0]][z[1]] = '@'

def hashLevel(boulders, holes, player):
	return hash(frozenset(boulders)) + hash(frozenset(holes)) + hash(player)
	
def findMoves(boulders, player, level):
	pr = player[0]
	pc = player[1]
	moves = []
	for b in boulders:
		r = b[0]
		c = b[1]
		if isStuck(r, c, level): return []
		if isClear(r-1, c, level) and canTravel(pr, pc, r+1, c, level):
			moves.append((r, c, r-1, c))
		if isClear(r+1, c, level) and canTravel(pr, pc, r-1, c, level):
			moves.append((r, c, r+1, c))
		if isClear(r, c-1, level) and canTravel(pr, pc, r, c+1, level):
			moves.append((r, c, r, c-1))
		if isClear(r, c+1, level) and canTravel(pr, pc, r, c-1, level):
			moves.append((r, c, r, c+1))
	return moves

def makeMove(move, level):
	r1 = move[0]
	c1 = move[1]
	r2 = move[2]
	c2 = move[3]
	level[r1][c1] = '.'
	if level[r2][c2] == '^':
		level[r2][c2] = '.'
	else:
		level[r2][c2] = '0'

def undoMove(move, level):
	r1 = move[0]
	c1 = move[1]
	r2 = move[2]
	c2 = move[3]
	level[r1][c1] = '0'
	if level[r2][c2] == '.'
		level[r2][c2] = '^'
	else
		level[r2][c2] = '.'

evaluated = set()
def solve(boulders, holes, player, level
	
	

if len(sys.argv) != 2:
	print('usage : sokobansolver level')
	quit()
fileName = sys.argv[1]
textFile = open(fileName)

level = readLevel(textFile)
boulders = listPositions('0', level)
holes = listPositions('^', level)
playerPos = findChar('@', level)
print(boulders)
print(holes)
print(hashLevel(boulders, holes, playerPos)) 
print(canTravel(playerPos[0], playerPos[1], 11, 2, level))

print(findMoves(boulders, playerPos, level))

