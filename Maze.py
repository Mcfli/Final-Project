import random


def generateMaze():
    dungeon = {}
    mustBeWall = False
    mazeStr = []
    block = ''
    spriteType = 0
    size = 20
    valid = False

    room1 = random.randint(1, size - 4)
    room2 = random.randint(1, size - 4)

    for i in xrange(size):
        if i == 0:
            horzWall = True
        elif i == size - 1:
            horzWall = True
        elif i in range(room1, room1 + 2):
            roomWall = True
        elif i in range(room2, room2 + 2):
            roomWall = True
        else:
            horzWall = False

        for j in xrange(size):
            if j == 0:
                vertWall = True
            elif j == size - 1:
                vertWall = True
            elif j in range(room1, room1 + 2):
                roomWall = True
            elif j in range(room2, room2 + 2):
                roomWall = True
            else:
                vertWall = False

            if vertWall or horzWall or roomWall:
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

            if i == 1 and j == 1:
                dungeon[(i, j)] = '@'

            if i == size - 2 and j == size - 2:
                dungeon[(i, j)] = '*'

    valid = dfs(dungeon, (1, 1), (size - 2, size - 2))

    if valid:
        for i in xrange(size):
            for j in xrange(size):
                block = block + dungeon[(i, j)] + ' '
            mazeStr.append(block)
            block = ''

        for i in mazeStr:
            print i
    else:
        generateMaze()


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
        if i != start or i != goal:
            graph[i] = "_"

    if goal in visited:
        return True
    else:
        return False


generateMaze()