from functools import reduce

# INPUT_FILE = "inputs/day11test.in"
INPUT_FILE = "inputs/day11.in"

part1 = [r[-1]*r[-2]for r in [sorted(m['b'] for m in reduce(lambda p,_:reduce(lambda m,n:{**m,n:{**m[n],'i':[],'b':m[n]['b']+len(m[n]['i'])},m[n]['t']:{**m[m[n]['t']],'i':m[m[n]['t']]['i']+[(lambda old:eval(m[n]['o']))(i) for i in m[n]['i']if not((lambda old:eval(m[n]['o']))(i))%m[n]['q']]},m[n]['f']:{**m[m[n]['f']],'i':m[m[n]['f']]['i']+[(lambda old:eval(m[n]['o']))(i) for i in m[n]['i']if((lambda old:eval(m[n]['o']))(i))%m[n]['q']]},},range(len(p)),p),range(20),{int(m[0][-2]):{'i':[int(i)for i in m[1][18:].split(', ')],'o':m[2][19:],'f':int(m[5][-1]),'q':int(m[3][20:]),'t':int(m[4][-1]),'b':0,}for m in [m.split('\n')for m in open(INPUT_FILE).read().split('\n\n')]}).values())]][0]
# part2 = [r[-1]*r[-2]for r in [sorted(m['b'] for m in reduce(lambda p,_:reduce(lambda m,n:{**m,n:{**m[n],'i':[],'b':m[n]['b']+len(m[n]['i'])},m[n]['t']:{**m[m[n]['t']],'i':m[m[n]['t']]['i']+[(lambda old:eval(m[n]['o']))(i)%reduce(lambda a,b:a*b,[x['q']for x in p.values()],1) for i in m[n]['i']if not((lambda old:eval(m[n]['o']))(i))%m[n]['q']]},m[n]['f']:{**m[m[n]['f']],'i':m[m[n]['f']]['i']+[(lambda old:eval(m[n]['o']))(i)%reduce(lambda a,b:a*b,[x['q']for x in p.values()],1) for i in m[n]['i']if((lambda old:eval(m[n]['o']))(i))%m[n]['q']]},},range(len(p)),p),range(10000),{int(m[0][-2]):{'i':[int(i)for i in m[1][18:].split(', ')],'o':m[2][19:],'f':int(m[5][-1]),'q':int(m[3][20:]),'t':int(m[4][-1]),'b':0,}for m in [m.split('\n')for m in open(INPUT_FILE).read().split('\n\n')]}).values())]][0]

print(part1)
print(part2)
