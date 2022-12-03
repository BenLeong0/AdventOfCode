a = 'sesenwnenenewseeswwswswwnenewsewsw'
arr = []

with open('inputs/day24.in') as f:
    line = f.readline()
    while line:
        line = line[:-1]
        i=0
        dir = []
        while i < len(line):
            if line[i] in ['w','e']:
                dir.append(line[i])
                i+=1
            else:
                dir.append(line[i:i+2])
                i+=2
        arr.append(dir)
        line = f.readline()


def partOne(arr=arr):
    blackTiles = set()
    for tile in arr:
        curr = [0,0,0]
        for dir in tile:
            if dir == 'e':
                curr[0] += 1
                curr[1] += 1
            elif dir == 'w':
                curr[0] -= 1
                curr[1] -= 1
            if dir == 'ne':
                curr[1] += 1
                curr[2] += 1
            elif dir == 'sw':
                curr[1] -= 1
                curr[2] -= 1
            elif dir == 'se':
                curr[0] += 1
                curr[2] -= 1
            elif dir == 'nw':
                curr[0] -= 1
                curr[2] += 1
        finalTile = tuple(curr)
        if finalTile not in blackTiles:
            blackTiles.add(finalTile)
        else:
            blackTiles.remove(finalTile)
    print('Black tiles in initial setup:', len(blackTiles))
    return blackTiles


def neighbours(tile):
    e   = (tile[0]+1,tile[1]+1,tile[2])
    w   = (tile[0]-1,tile[1]-1,tile[2])
    ne  = (tile[0],tile[1]+1,tile[2]+1)
    sw  = (tile[0],tile[1]-1,tile[2]-1)
    se  = (tile[0]+1,tile[1],tile[2]-1)
    nw  = (tile[0]-1,tile[1],tile[2]+1)
    return (e,w,ne,sw,se,nw)


def partTwo(blackTiles,days=100):
    for _ in range(days):
        whiteTiles = set()
        newBlackTiles = set()
        for tile in blackTiles:
            blackCount = 0             # number of black adjacents
            for n in neighbours(tile):
                if n not in blackTiles:
                    whiteTiles.add(n)
                else:
                    blackCount += 1
            if blackCount in [1,2]:
                newBlackTiles.add(tile)

        for tile in whiteTiles:
            blackCount = 0
            for n in neighbours(tile):
                if n in blackTiles:
                    blackCount += 1
            if blackCount == 2:
                newBlackTiles.add(tile)

        blackTiles = newBlackTiles
    return print('Black tiles after', days, 'days:', len(blackTiles))


partTwo(partOne())
