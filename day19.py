rules = {}
messages = []

with open("inputs/day19input", 'r') as f:
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

print(rules)

def partOne(n=0):
    if type(rules[n]) == str:
        return {rules[n]}
    results = []
    for rule in rules[n]:
        curr = ['']
        for i in rule.split(' '):
            current
