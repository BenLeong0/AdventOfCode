with open('day22.in') as f:
    line = f.readline()
    line = f.readline()
    p1 = []
    while line != '\n':
        p1.append(int(line[:-1]))
        line = f.readline()
    line = f.readline()
    line = f.readline()
    p2 = []
    while line:
        p2.append(int(line[:-1]))
        line = f.readline()


def partOne(p1=p1[:], p2=p2[:]):
    while p1 and p2:
        if p1[0] > p2[0]:
            p1 = p1[1:] + [p1[0], p2[0]]
            p2 = p2[1:]
        elif p2[0] > p1[0]:
            p2 = p2[1:] + [p2[0], p1[0]]
            p1 = p1[1:]
    if p1:
        print('Player 1 deck:', p1)
        return print('Score:', sum([i*j for (i,j) in enumerate(p1[::-1], start=1)]))
    elif p2:
        print('Player 2 deck:', p2)
        return print('Score:', sum([i*j for (i,j) in enumerate(p2[::-1], start=1)]))


def partTwo(p1=p1[:], p2=p2[:], first=True):
    hands = []
    while p1 and p2:
        if (p1,p2) in hands:
            if first:
                print('[Infinite loop]')
                print('Player 1 deck:', p1)
                return print('Score:', sum([i*j for (i,j) in enumerate(p1[::-1], start=1)]))
            return 1
        hands.append((p1,p2))

        if len(p1) > p1[0] and len(p2) > p2[0]:
            subgame = partTwo(p1=p1[1:p1[0]+1], p2=p2[1:p2[0]+1], first=False)
            if subgame == 1:
                p1 = p1[1:] + [p1[0], p2[0]]
                p2 = p2[1:]
            elif subgame == 2:
                p2 = p2[1:] + [p2[0], p1[0]]
                p1 = p1[1:]

        else:
            if p1[0] > p2[0]:
                p1 = p1[1:] + [p1[0], p2[0]]
                p2 = p2[1:]
            elif p2[0] > p1[0]:
                p2 = p2[1:] + [p2[0], p1[0]]
                p1 = p1[1:]

    if p1:
        if first:
            print('Player 1 deck:', p1)
            return print('Score:', sum([i*j for (i,j) in enumerate(p1[::-1], start=1)]))
        return 1
    elif p2:
        if first:
            print('Player 2 deck:', p2)
            return print('Score:', sum([i*j for (i,j) in enumerate(p2[::-1], start=1)]))
        return 2



partOne()
print()
partTwo()
