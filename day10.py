values = []

with open('inputs/day10input', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        line = line[:-1]
        values.append(int(line))

values.sort()
values = [0] + values + [values[-1] + 3]

def partOne(values=values):
    count = 0
    differences = {1:0, 2:0, 3:0}
    for i in range(len(values) - 1):
        differences[values[i+1] - values[i]] += 1
    return differences[1]*differences[3]


def partTwo(values=values, index=1, routeCounts=[1]):
    routeCounts.append(0)
    for i in range(max(0, index-3), index):
        if values[i] >= values[index] - 3:
            routeCounts[-1] += routeCounts[i]
    if index == len(values) - 1:
        return routeCounts[-1]
    return partTwo(index=index+1, routeCounts=routeCounts)


print('There are', partOne(), '1-jolt differences.')
print('There are', partTwo(), 'possible adapter combinations.')


# [(0) 1 4 5 6 7 10 11 12 15 16 19 (22)]
