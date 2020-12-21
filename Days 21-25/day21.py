
def f(part=1):
    foods = []      # [({ingredients}, {allergens}), ...]
    a = set()       # {allergens}
    bad = []        # [(code, allergen), ...]
    with open('day21.in') as f:
        line = f.readline()
        while line:
            line = line[:-2]
            x = line.split(' (contains ')
            x = (set(x[0].split(' ')), set(x[1].split(', ')))
            foods.append(x)
            a = a.union(x[1])
            line = f.readline()

    while a:
        for al in a:
            curr = []
            for food in foods:
                if al in food[1]:
                    curr.append(food[0])
            if len(curr) < 1:
                continue
            i = curr[0]
            for food in curr[1:]:
                i = i.intersection(food)
            if len(i) == 1:
                i = i.pop()
                a.remove(al)
                bad.append((i,al))
                for food in foods:
                    if i in food[0]:
                        food[0].remove(i)
                break

    if part == 1:
        count = 0
        for food in foods:
            count += len(food[0])
        return print("Part one:", count)
    elif part == 2:
        bad.sort(key=lambda x: x[1])
        return print("Part two:", ','.join([x[0] for x in bad]))


def partOne():
    return f(part=1)

def partTwo():
    return f(part=2)


partOne()
print()
partTwo()
