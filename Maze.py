import random
import math
import string


def generateMaze(inputRoomA = [], inputRoom1 = 0, inputDoorPosA = (0, 0), inputFlag = False):
    dungeon = {}
    mustBeWall = False
    mazeStr = []
    block = ''
    spriteType = 0
    size = 20
    valid = False
    roomA = inputRoomA
    roomB = []
    
    room1 = inputRoom1
    if room1 == 0: #if room1Coord not input
        room1 = random.randint(1, size - 4)
    room2 = random.randint(1, size - 4)
    while (abs(room2 - room1) < 3): #pretty sure this prevents the rooms from overlapping
        room2 = random.randint(1, size - 4)

    for i in xrange(size):
        if i == 0:
            horzWall = True
        elif i == size - 1:
            horzWall = True
        else:
            horzWall = False

        for j in xrange(size):
            if j == 0:
                vertWall = True
            elif j == size - 1:
                vertWall = True
            else:
                vertWall = False

            if vertWall or horzWall:
                mustBeWall = True
            else:
                mustBeWall = False

            if mustBeWall:
                spriteType = 0
            else:
                spriteType = random.randint(0, 1)

            if spriteType == 0:
                dungeon[(i, j)] = 'W'
            elif spriteType == 1:
                dungeon[(i, j)] = '.'
            elif spriteType == 2:
                dungeon[(i, j)] = 'D'

    if not roomA: #if an initial room was not given to the generator
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                roomA.append((room1 + i, room1 + j))
                roomB.append((room2 + i, room2 + j))
    else: #initial room was given to generator as roomA
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                roomB.append((room2 + i, room2 + j))

    doorAX = random.randint(-1,1)
    doorAY = random.randint(-1,1)
    doorBX = random.randint(-1,1)
    doorBY = random.randint(-1,1)

    doorPosA = inputDoorPosA
    if doorPosA == (0, 0): #if doorPosA not input
        doorPosA = (room1 + doorAX, room1 + doorAY)
    doorPosB = (room2 + doorBX, room2 + doorBY)

    for i in roomA:
        if i == (room1, room1):
            dungeon[i] = '@'
        elif i == doorPosA:
            dungeon[i] = 'D'
        else:
            dungeon[i] = 'W'

    for j in roomB:
        if j == (room2, room2):
            dungeon[j] = '*'
        elif j == doorPosB:
            dungeon[j] = 'D'
        else:
            dungeon[j] = 'W'


    valid = dfs(dungeon, (room1, room1), (room2, room2))

    if valid:
        for i in xrange(size):
            for j in xrange(size):
                block = block + dungeon[(i, j)] + ' '
            mazeStr.append(block)
            block = ''

        for i in mazeStr:
            print i
        returnDict = {}
        returnDict["roomB"] = roomB
        returnDict["roomBCoord"] = room2
        returnDict["doorPosB"] = doorPosB
        return returnDict
    else:
        if inputFlag:
            return generateMaze(roomA, room1, doorPosA, True)
        else:
            #for some reason these default inputs need to be included
            #else they get overwritten by the previous values
            return generateMaze([], 0, (0, 0), False) 


def getNeighbors(graph, node):
    steps = []
    x, y = node
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            next_node = (x + dx, y + dy)
            if next_node in graph:
                steps.append(next_node)
    return steps


def dfs(graph, start, goal):
    visited, stack = [], [start]
    path = []
    while stack:
        vertex = stack.pop()

        if goal == vertex:
            visited.append(vertex)
            break

        neighbors = getNeighbors(graph, vertex)
        for next_node in neighbors:
            if next_node not in visited and graph[next_node] != 'W':
                visited.append(vertex)
                stack.append(next_node)
                if vertex != start:
                    path.append(vertex)

    for i in path:
        if i != start and i != goal:
            graph[i] = "_"

    if goal in visited:
        return True
    else:
        return False


state = generateMaze()
while True:
    print "Enter anything to generate a new, constrained maze."
    inputString = raw_input("> ")
    if inputString == "exit":
        break;
    state = generateMaze(state["roomB"], state["roomBCoord"], state["doorPosB"], True)