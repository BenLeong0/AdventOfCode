def partOne():
    with open('day07.in', 'r') as f:
        parents = {}
        while True:
            line = f.readline()
            if not line:
                break
            line = line[:-1]
            [parent, childlist] = line.split(' bags contain ')
            if childlist == "no other bags.":
                continue
            else:
                children = [child.split(' ')[1] + ' ' + child.split(' ')[2] for child in childlist.split(', ')]
                for child in children:
                    if child not in parents:
                        parents[child] = {parent}
                    else:
                        parents[child].add(parent)

    def find_ancestors(x, covered = set()):
        covered.add(x)
        if x in parents:
            parentList = {parent for parent in parents[x]}
            list = {x}
            for parent in parentList:
                if parent not in covered:
                    list = list.union(find_ancestors(parent))
            return list
        else:
            return {x}

    def get_ancestors(x):
        list = find_ancestors(x)
        list.remove(x)
        return len(list)

    print(get_ancestors("shiny gold"))


def partTwo():
    with open('day07.in', 'r') as f:
        parents = {}
        while True:
            line = f.readline()
            if not line:
                break
            line = line[:-1]
            [parent, childlist] = line.split(' bags contain ')
            if childlist == "no other bags.":
                parents[parent] = []
            else:
                children = [(child.split(' ')[0], child.split(' ')[1] + ' ' + child.split(' ')[2]) for child in childlist.split(', ')]
                parents[parent] = children


    def numberOfChildren(x, first=False):
        if parents[x]:
            return sum([int(y[0]) * numberOfChildren(y[1]) for y in parents[x]])+1-first
        else:
            return 1-first

    print(numberOfChildren('shiny gold', first=True))


partOne()
partTwo()
