import networkx as nx

with open('day16.in', 'r') as f:
    line = f.readline()
    status = 'rules'
    rules = {}
    nearbyTickets = []
    while line:
        line = line[:-1]
        if line == '':
            pass
        elif line == 'your ticket:':
            status = 'ownTicket'
        elif line == 'nearby tickets:':
            status = 'nearbyTickets'
        elif status == 'rules':
            lineSplit = line.split(' ')
            orIndex = lineSplit.index('or')
            rules[line.split(':')[0]] = [[tuple(int(x) for x in lineSplit[orIndex+i].split('-')) for i in [-1,1]], -1]
        elif status == 'ownTicket':
            ownTicket = [int(x) for x in line.split(',')]
        elif status == 'nearbyTickets':
            nearbyTickets.append([int(x) for x in line.split(',')])

        line = f.readline()


def validValue(value):
    for rule in rules.values():
        for (a,b) in rule[0]:
            if a<=value<=b:
                return True
    return False


def errorsCheck(ticket, part, rules=rules):
    total = 0
    for value in ticket:
        if not validValue(value):
            total += value

    total = total if part == 1 else total==0
    return total


def partOne():
    total = 0
    for ticket in nearbyTickets:
        total += errorsCheck(ticket, part=1)
    return print(total)




def partTwo():
    validTickets = [ownTicket]


    for ticket in nearbyTickets:
        if sum([1 for value in ticket if validValue(value) == False]) == 0:
            validTickets.append(ticket)

    def ruleCheck(values, rule):
        ruleBounds = rule[1][0]
        a,b,c,d = ruleBounds[0][0], ruleBounds[0][1], ruleBounds[1][0], ruleBounds[1][1]
        for value in values:
            if not (a<=value<=b or c<=value<=d):
                return False
        return True

    edgelist = []
    for i in range(len(ownTicket)):
        for rule in rules.items():
            if ruleCheck([ticket[i] for ticket in validTickets], rule):
                edgelist.append((rule[0], i))
    # print(edgelist.sort(key = lambda x : x[0]))
    print(edgelist)
    G = nx.Graph(edgelist)
    nodes = list(G.nodes)
    matching = []
    while nodes:
        for node in nodes:
            if G.degree(node) == 1:
                otherNode = list(G.neighbors(node))[0]
                matching.append((node, otherNode))
                nodes.remove(node)
                nodes.remove(otherNode)
                G.remove_node(node)
                G.remove_node(otherNode)
                break

    result = 1
    for match in matching:
        if match[0][:9] == 'departure':
            result *= ownTicket[match[1]]
    return print(result)

partOne()
partTwo()
