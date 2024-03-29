from math import log

rules = {}
ruleSizes = {}
messages = []

with open('inputs/day19.in', 'r') as f:
    line = f.readline()
    while line != '\n':
        line = line[:-1].split(': ')
        if line[1].count('"') > 0:
            rules[line[0]] = line[1][1]
        else:
            rules[line[0]] = line[1].split(' | ')
        line = f.readline()
    line=f.readline()
    while line:
        messages.append(line[:-1])
        line = f.readline()


def f(s, rule='0', rules=rules):
    options = rules[rule]
    if not s:
        return (False, '')
    if type(options) == str:
        if s[0] == options:
            return (True, s[1:])
        return (False, s)
    for option in options:
        curr = s
        fail = False
        for r in option.split(' '):
            check = f(curr, rule=r, rules=rules)
            if check[0]:
                curr = check[1]
            else:
                fail = True
                break
        if not fail:
            if rule=='0' and curr:
                continue
            else:
                return (True, curr)
    return (False, s)


def partOne():
    count = 0
    for message in messages:
        if f(message)[0]:
            count += 1
    return print(count)


def partTwo():
    # Not sure if this is good method for finding limit lol
    limit = 0
    for message in messages:
        limit = max(limit, int(log(len(message),2))+2)
    print('Limit:', limit)

    newRules = rules.copy()
    options = newRules['0']
    s = options[0]
    while len(options) < limit:
        s = s.replace('8', '42 8')
        options.append(s)
    for i in range(limit):
        s = options[i]
        while len(s.split(' ')) < limit:
            s = s.replace('11', '42 11 31')
            options.append(s)
    newRules['0'] = options

    count = 0
    for message in messages:
        if f(message, rules=newRules)[0]:
            count += 1
    return print(count)


partOne()
partTwo()
