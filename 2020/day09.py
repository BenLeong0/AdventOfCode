values = []
sums = []
n = 25

with open('inputs/day09.in', 'r') as f:
    line = f.readline()
    while line:
        line = line[:-1]
        values.append(int(line))
        line = f.readline()

for i in range(n-1):
    sumList = []
    for j in range(i+1, n):
        sumList.append(values[i] + values[j])
    sums.append(sumList)


def isSum(values, sums=sums, index=n):
    value = values[index]
    check = sum([value in x for x in sums])
    if check > 0:       # Is present
        sums = sums[1:] + [[]]
        for i in range(n-1):
            sums[i].append(values[index + i - (n-1)] + value)
        return isSum(values, sums, index + 1)
    else:
        return value


def findSet(values, index=0, error=isSum(values)):
    total = values[index]
    i = index + 1
    while True:
        total += values[i]
        if total == error:
            valueRange = values[index:i+1]
            return min(valueRange) + max(valueRange)
        elif total > error:
            return findSet(values, index+1)
        i += 1


print(isSum(values))
print(findSet(values))
