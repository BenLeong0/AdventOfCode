line = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"


def parseLine(line, i=0, part=1):
    curr = []
    while i < len(line):
        if line[i] == ' ':
            pass
        elif line[i] == '(':
            newLine, newPos = parseLine(line, i=i+1, part=part)
            curr.append(newLine)
            i = newPos
        elif line[i] == ')':
            if part == 2:
                while curr.count('+') != 0:
                    id = curr.index('+')
                    curr = curr[:id-1] + [[curr[id-1], '+', curr[id+1]]] + curr[id+2:]
            return curr, i
        elif line[i] in ['*', '+']:
            curr.append(line[i])
        else:
            curr.append(int(line[i]))
        i += 1
    if part == 2:
        while curr.count('+') != 0:
            id = curr.index('+')
            curr = curr[:id-1] + [[curr[id-1], '+', curr[id+1]]] + curr[id+2:]
    return curr


def evalParsed(line):
    if type(line) is int:
        return line
    result = evalParsed(line[0])
    for i in range(1, len(line), 2):
        if line[i] == '*':
            result *= evalParsed(line[i+1])
        elif line[i] == '+':
            result += evalParsed(line[i+1])
    return result


def partOne(part=1):
    result = 0
    with open('day18.in', 'r') as f:
        line = f.readline()
        while line:
            result += evalParsed(parseLine(line[:-1],part=part))
            line = f.readline()
    return print(result)

def partTwo():
    return partOne(part=2)


partOne()
partTwo()
