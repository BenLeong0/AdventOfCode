def partOne():
    mem = {}
    with open('inputs/day14.in', 'r') as f:
        line = f.readline()[:-1]
        while line:
            if line.split(' ')[0] == 'mask':
                # Save mask as dict, with pos:bit
                mask = {key:value for (key, value) in enumerate(line.split(' ')[2]) if value!='X'}

            else:
                # Convert to binary
                b = format(int(line.split(' ')[2]), '036b')
                # Apply each element of the mask
                for (key,value) in mask.items():
                    b = b[:key] + value + b[key+1:]
                # Convert back to decimal and save to mem(ory)
                mem[line.split(' ')[0][4:-1]] = int(b,2)

            line = f.readline()[:-1]
    return print('Part One:  ', sum(mem.values()))


def partTwo():
    mem = {}
    with open('inputs/day14.in', 'r') as f:
        line = f.readline()[:-1]
        while line:
            if line.split(' ')[0] == 'mask':
                # Save mask as dict, with pos:bit
                mask = {key:value for (key, value) in enumerate(line.split(' ')[2])}

            else:
                # Convert address to binary and place in array
                a = [format(int(line.split(' ')[0][4:-1]), '036b')]
                for (key,value) in mask.items():
                    if value == '1':
                        # Update each element of array
                        a = [x[:key] + '1' + x[key+1:] for x in a]
                    elif value == 'X':
                        # If value=X, clone all elements of array with pos = 0 and 1
                        a = [x[:key] + '1' + x[key+1:] for x in a] + [x[:key] + '0' + x[key+1:] for x in a]

                # Convert all addresses back to decimal and save values
                for address in a:
                    mem[int(address,2)] = int(line.split(' ')[2])

            line = f.readline()[:-1]
    return print('Part Two:  ', sum(mem.values()))


partOne()
partTwo()
