def partOne():
    mem = {}
    with open('inputs/day14input', 'r') as f:
        line = f.readline()[:-1]
        while line:
            if line.split(' ')[0] == 'mask':
                mask = {key:value for (key, value) in enumerate(line.split(' ')[2]) if value!='X'}
            else:
                b = format(int(line.split(' ')[2]), '036b')
                for (key,value) in mask.items():
                    b = b[:key] + value + b[key+1:]
                mem[line.split(' ')[0][4:-1]] = int(b,2)
            line = f.readline()[:-1]
    return print('Part One:  ', sum(mem.values()))


def partTwo():
    mem = {}
    with open('inputs/day14input', 'r') as f:
        line = f.readline()[:-1]
        while line:
            if line.split(' ')[0] == 'mask':
                mask = {key:value for (key, value) in enumerate(line.split(' ')[2])}
            else:
                a = [format(int(line.split(' ')[0][4:-1]), '036b')]
                for (key,value) in mask.items():
                    if value == '1':
                        a = [x[:key] + '1' + x[key+1:] for x in a]
                    elif value == 'X':
                        a = [x[:key] + '1' + x[key+1:] for x in a] + [x[:key] + '0' + x[key+1:] for x in a]
                for address in a:
                    mem[int(address,2)] = int(line.split(' ')[2])
            line = f.readline()[:-1]
    return print('Part Two:  ', sum(mem.values()))


partOne()
partTwo()
