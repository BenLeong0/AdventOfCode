from math import inf

instructions = []

with open('day13.in', 'r') as f:
    startTime = int(f.readline())
    timeList = f.readline()
    if timeList[-1] == '\n':
        timeList = timeList[:-1]
    times = [int(x) if x != 'x' else x for x in timeList.split(',')]


def partOne():
    min = (0, inf)
    for id in (x for x in times if x != 'x'):
        if id - startTime%id < min[1]:
            min = (id, id - startTime%id)
    print(min, '=>', min[0]*min[1])
    return


def partTwo():
    newStart = 0
    inc = 1
    for (i, id) in enumerate(times):
        if id != 'x':
            while (id - newStart%id)%id != i%id:
                newStart += inc
            inc *= id
    print(newStart)
    return


partOne()
partTwo()
