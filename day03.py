count11 = 0
count31 = 0
count51 = 0
count71 = 0
count12 = 0
i = 0

with open('inputs/day03input', 'r') as f:
    while True:
        line = f.readline()[:-1]
        if not line:
            break
        width = len(line)
        if line[(1*i)%width] == '#':
            count11 += 1;
        if line[(3*i)%width] == '#':
            count31 += 1;
        if line[(5*i)%width] == '#':
            count51 += 1;
        if line[(7*i)%width] == '#':
            count71 += 1;
        if (i%2 == 0):
            if line[int(i/2)%width] == '#':
                count12 += 1;

        i += 1

count = count11 * count31 * count51 * count71 * count12
print(count)
