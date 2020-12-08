from copy import deepcopy

accumulator = 0
instructions = []

with open('day08input', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        line = line[:-1]
        instructions.append(line.split(' ') + [False])


def f(array, i=0, acc=0):
    if array[i][2]:
        return 0
    else:
        array[i][2] = True
        if array[i][0] == 'acc':
            acc += int(array[i][1])
            n = i + 1
        elif array[i][0] == 'jmp':
            n = i + int(array[i][1])
        elif array[i][0] == 'nop':
            n = i + 1
        if n == len(array):
            print('Acculator value after fixing:', acc)
            return 1
        return f(array, n, acc)


toggle = {'jmp': 'nop', 'nop': 'jmp'}


for k in range(len(instructions)):
    newArray = deepcopy(instructions)
    if newArray[k][0] == 'acc':
        continue
    elif newArray[k][0] in toggle:
        newArray[k][0] = toggle[newArray[k][0]]
        if f(newArray):
            break
        newArray[k][0] = toggle[newArray[k][0]]
