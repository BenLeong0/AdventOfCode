seats = []

with open('inputs/day11input', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        line = line[:-1]
        seats.append(list(line))


height = len(seats)
width = len(seats[0])
print(height, width)


def getAdjacents(row,col):
    adjacents = []
    for i in range(-1,2):
        for j in range(-1,2):
            if i==j==0:
                continue
            if row+i < 0 or row+i >= height:
                continue
            if col+j < 0 or col+j >= width:
                continue
            adjacents.append((row+i,col+j))
    return adjacents


def partOne(seats=seats):
    newSeats = [row[:] for row in seats]
    for i in range(height):
        for j in range(width):
            if newSeats[i][j] == '.':
                continue
            adjStates = []
            for (x,y) in getAdjacents(i,j):
                adjStates.append(seats[x][y])
            if seats[i][j] == 'L':
                if adjStates.count('#') == 0:
                    newSeats[i][j] = '#'
            elif seats[i][j] == '#':
                if adjStates.count('#') >= 4:
                    newSeats[i][j] = 'L'
    if newSeats == seats:
        return sum(row.count('#') for row in newSeats)
    else:
        return partOne(seats=newSeats)


def partTwo(seats=seats):
    newSeats = [row[:] for row in seats]
    for i in range(height):
        for j in range(width):
            if newSeats[i][j] == '.':
                continue
            adjStates = {'L': 0, '#': 0}
            for direction in [(x,y) for x in range(-1,2) for y in range(-1,2) if not (x==y==0)]:
                x = i+direction[0]
                y = j+direction[1]
                while True:
                    if x < 0 or x >= height or y < 0 or y >= width:
                        break
                    elif seats[x][y] == '.':
                        x += direction[0]
                        y += direction[1]
                    else:
                        adjStates[seats[x][y]] += 1
                        break
            if seats[i][j] == 'L':
                if adjStates['#'] == 0:
                    newSeats[i][j] = '#'
            elif seats[i][j] == '#':
                if adjStates['#'] >= 5:
                    newSeats[i][j] = 'L'
    if newSeats == seats:
        return sum(row.count('#') for row in newSeats)
    else:
        return partTwo(seats=newSeats)



print(partOne())
print(partTwo())
