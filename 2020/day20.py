from math import sqrt

with open('inputs/day20.in') as f:
    idLine = True
    tiles = {}
    fullTiles = {}
    line = f.readline()
    while line:
        if idLine:
            idLine = False
            id = line[5:9]
            lines = []
        elif line == '\n':
            idLine = True
            sides = [   lines[0],
                        ''.join([x[-1] for x in lines]),
                        lines[-1][::-1],
                        ''.join([x[0] for x in lines])[::-1] ]
            tiles[int(id)] = sides
            fullTiles[int(id)] = lines
        else:
            lines.append(line[:-1])
        line = f.readline()
    tiles[int(id)] = [   lines[0],
                    ''.join([x[-1] for x in lines]),
                    lines[-1][::-1],
                    ''.join([x[0] for x in lines])[::-1] ]
    fullTiles[int(id)] = lines


def orientations(tile):
    reflected = [tile[0][::-1], tile[3][::-1], tile[2][::-1], tile[1][::-1]]
    a = [tile[i:] + tile[:i] for i in range(len(tile))]
    b = [reflected[i:] + reflected[:i] for i in range(len(reflected))]
    return a + b


width = int(sqrt(len(tiles)))


def partOne(setup=[[]], tiles=tiles):
    if len(tiles) == 0:
        # Finished
        return 1
    currSetup = [row[:] for row in setup]
    for tile in tiles.items():
        currTiles = tiles.copy()
        del currTiles[tile[0]]
        for o in orientations(tile[1]):
            # Empty
            if setup == [[]]:
                result = partOne(setup=[[o]], tiles=currTiles)
                if result:
                    # Top left corner
                    return print(result * tile[0])
            # Row full
            elif len(setup[-1]) == width:
                if setup[-1][0][2] == o[0][::-1]:
                    result = partOne(setup=setup+[[o]], tiles=currTiles)
                    if result:
                        if len(setup) == width-1:
                            # Bottom left corner
                            return result * tile[0]
                        return result
            # Past first row
            elif len(setup) > 1:
                if setup[-1][-1][1] == o[3][::-1] and setup[-2][len(setup[-1])][2] == o[0][::-1]:
                    result = partOne(setup=setup[:-1]+[setup[-1]+[o]], tiles=currTiles)
                    if result:
                        if len(setup) == width and len(setup[-1]) == width-1:
                            # Bottom right corner
                            return result * tile[0]
                        return result
            # First row, not yet filled
            else:
                if setup[-1][-1][1] == o[3][::-1]:
                    result = partOne(setup=[setup[-1]+[o]], tiles=currTiles)
                    if result:
                        if len(setup[-1]) == width-1:
                            # Top right corner
                            return result * tile[0]
                        return result
    return False

def previd(tile,i,j):
    width = len(tile)
    i -= (width-1)/2
    j -= (width-1)/2
    i,j = j,-i
    i = int(i + (width-1)/2)
    j = int(j + (width-1)/2)
    return i,j


def getOriented(tile, o_id, part=True):
    if o_id > 3:
        tile = [row[::-1] for row in tile]
    o_id %= 4
    if part:
        width = len(tile)
    else:
        width = len(tile[0])
    for _ in range(o_id):
        tile = [[tile[previd(tile,i,j)[0]][previd(tile,i,j)[1]] for j in range(width)] for i in range(width)]
    if part:
        return [''.join(row[1:-1]) for row in tile[1:-1]]
    else:
        return [''.join(row) for row in tile]


def f(setup=[[]], tiles=tiles):
    if len(tiles) == 0:
        # Finished
        return (1, [[]])
    currSetup = [row[:] for row in setup]
    for tile in tiles.items():
        currTiles = tiles.copy()
        del currTiles[tile[0]]
        for (i,o) in enumerate(orientations(tile[1])):
            # Empty
            if setup == [[]]:
                result = f(setup=[[o]], tiles=currTiles)
                if result:
                    # Top left corner
                    print('Product of corners:', result[0] * tile[0])
                    return [[(i,tile[0])] + result[1][0]] + result[1][1:]
            # Row full
            elif len(setup[-1]) == width:
                if setup[-1][0][2] == o[0][::-1]:
                    result = f(setup=setup+[[o]], tiles=currTiles)
                    if result:
                        a = result[0]
                        b = [[], [(i,tile[0])] + result[1][0]] + result[1][1:]
                        if len(setup) == width-1:
                            # Bottom left corner
                            a *= tile[0]
                        return a,b
            # Past first row
            elif len(setup) > 1:
                if setup[-1][-1][1] == o[3][::-1] and setup[-2][len(setup[-1])][2] == o[0][::-1]:
                    result = f(setup=setup[:-1]+[setup[-1]+[o]], tiles=currTiles)
                    if result:
                        a = result[0]
                        b = [[(i,tile[0])] + result[1][0]] + result[1][1:]
                        if len(setup) == width and len(setup[-1]) == width-1:
                            # Bottom right corner
                            a *= tile[0]
                        return a,b
            # First row, not yet filled
            else:
                if setup[-1][-1][1] == o[3][::-1]:
                    result = f(setup=[setup[-1]+[o]], tiles=currTiles)
                    if result:
                        a = result[0]
                        b = [[(i,tile[0])] + result[1][0]] + result[1][1:]
                        if len(setup[-1]) == width-1:
                            # Top right corner
                            a *= tile[0]
                        return a,b
    return False


def checkSerpents(photo):
    photo = [[i for i in row] for row in photo]
    for (i,row) in enumerate(photo[:-2]):
        for (j,letter) in enumerate(row):
            if 18 <= j < len(row):
                if letter == '#':
                    if (photo[i+1][j-18] == '#'
                        and photo[i+2][j-17] == '#'
                        and photo[i+2][j-14] == '#'
                        and photo[i+1][j-13] == '#'
                        and photo[i+1][j-12] == '#'
                        and photo[i+2][j-11] == '#'
                        and photo[i+2][j-8] == '#'
                        and photo[i+1][j-7] == '#'
                        and photo[i+1][j-6] == '#'
                        and photo[i+2][j-5] == '#'
                        and photo[i+2][j-2] == '#'
                        and photo[i+1][j-1] == '#'
                        and photo[i+1][j] == '#'
                        and photo[i+1][j+1] == '#'):
                        photo[i][j] = 'O'
                        photo[i+1][j-18] = 'O'
                        photo[i+2][j-17] = 'O'
                        photo[i+2][j-14] = 'O'
                        photo[i+1][j-13] = 'O'
                        photo[i+1][j-12] = 'O'
                        photo[i+2][j-11] = 'O'
                        photo[i+2][j-8] = 'O'
                        photo[i+1][j-7] = 'O'
                        photo[i+1][j-6] = 'O'
                        photo[i+2][j-5] = 'O'
                        photo[i+2][j-2] = 'O'
                        photo[i+1][j-1] = 'O'
                        photo[i+1][j] = 'O'
                        photo[i+1][j+1] = 'O'
    return [''.join(row) for row in photo]



def partTwo():
    setup = f()
    photoTiles = [[getOriented(fullTiles[tile],o_id) for (o_id,tile) in row] for row in setup]
    photo = []
    for tileRow in photoTiles:
        for i in range(len(tileRow[0])):
            photo.append(''.join([tile[i] for tile in tileRow]))
    for i in range(4):
        photo = getOriented(photo, 1, False)
        photo = checkSerpents(photo)
    photo = getOriented(photo, 4, False)
    for i in range(4):
        photo = getOriented(photo, 1, False)
        photo = checkSerpents(photo)


    count = 0
    print('Final image:')
    for row in photo:
        print(row)
        for i in row:
            if i == '#':
                count += 1
    return print('Roughness:', count)

partTwo()
