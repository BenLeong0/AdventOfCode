
start = [19,20,14,0,9,1]


def f(n, start=start):
    mem = {val:i+1 for (i,val) in enumerate(start[:-1])}
    prev = start[-1]
    i = len(start)

    while i < n:
        if prev not in mem:
            mem[prev], prev = i, 0
        else:
            mem[prev], prev = i, i-mem[prev]
        i+=1

    return print('Input:', start, '\n{}th number:'.format(n), prev)


def partOne():
    print('Part one:')
    return f(2020)


def partTwo():
    print('Part two:')
    return f(30000000)


partOne()
print('===========')
partTwo()
