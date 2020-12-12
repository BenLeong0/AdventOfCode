instructions = []

with open('inputs/day12input', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        line = line[:-1]
        instructions.append((line[0], int(line[1:])))


# Values are (xy-component, sign)
dirs = {'E': (0,1), 'W': (0,-1), 'N': (1,1), 'S': (1,-1)}
cards = ['N','E','S','W']


def partOne():
    dir = 'E'
    pos = [0,0]
    for x in instructions:
        if x[0] == 'F':
            pos[dirs[dir][0]] += dirs[dir][1] * x[1]
        elif x[0] in dirs.keys():
            pos[dirs[x[0]][0]] += dirs[x[0]][1] * x[1]
        elif x[0] in ['L','R']:
            dir = cards[(cards.index(dir) + (-1)**(x[0]!='R')*int(x[1]/90)) % 4]
    print('Part 1 position:', pos)
    print('Distance:', abs(pos[0]) + abs(pos[1]))


def partTwo():
    pos = [0,0]
    wpos = [10,1]
    for x in instructions:
        if x[0] == 'F':
            pos = [pos[i] + wpos[i]*x[1] for i in [0,1]]
        elif x[0] in dirs.keys():
            wpos[dirs[x[0]][0]] += dirs[x[0]][1] * x[1]
        elif x[0] in ['L','R']:
            for _ in range(((-1)**(x[0]!='R')*int(x[1]/90)) % 4):
                wpos = [wpos[1], -wpos[0]]
    print('Part 2 position:', pos)
    print('Distance:', abs(pos[0]) + abs(pos[1]))


partOne()
print()
partTwo()
