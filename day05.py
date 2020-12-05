from math import inf

seats = []

with open('day05input', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        seats.append(line[:-1])

print(seats)

def decodeRow(x):
    return int(x[:-3].replace('F','0').replace('B','1'), 2)

def decodeColumn(x):
    return int(x[-3:].replace('L','0').replace('R','1'), 2)

def getId(x):
    return int(x.replace('F','0').replace('B','1').replace('L','0').replace('R','1'), 2)


maxId = 0
minId = inf

ids = []

# for seat in seats:
#     if getId(seat) > maxId:
#         maxId = getId(seat)

for seat in seats:
    ids.append(getId(seat))

ids.sort()

i = 13
for id in ids:
    if id != i:
        print(i)
        break
    i += 1


print(maxId)
