from datetime import datetime

start = [19,20,14,0,9,1]


def f(n, start=start):
    startTime = datetime.now()
    mem = {val:i+1 for (i,val) in enumerate(start[:-1])}
    prev = start[-1]

    for i in range(len(start), n):
        if prev not in mem:
            mem[prev], prev = i, 0
        else:
            mem[prev], prev = i, i-mem[prev]


    print('Input:', start)
    print('{}th number:'.format(n), prev)
    print('Time taken:', (datetime.now() - startTime).total_seconds(), 'seconds')
    return


def partOne():
    print('Part one:')
    return f(2020)


def partTwo():
    print('Part two:')
    return f(30000000)


partOne()
print('===========')
partTwo()
