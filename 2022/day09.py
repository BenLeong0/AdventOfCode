from functools import reduce

# INPUT_FILE = "inputs/day09test.in"
INPUT_FILE = "inputs/day09.in"

part1 = len(reduce(lambda c,p:{**c,0:(c[0][0]+({"R":1,"L":-1}.get(p,0)),c[0][1]+({"U":1,"D":-1}.get(p,0)))}if p in "RULD" else{**c,"":c[''].union({c[1]})}if p=="c"else{**c,int(p):(lambda x,y:y if abs(x[0]-y[0])<2 and abs(x[1]-y[1])<2 else(y[0]-1 if y[0]-x[0]>0 else y[0]+1 if x[0]-y[0]>0 else y[0],y[1]-1 if y[1]-x[1]>0 else y[1]+1 if x[1]-y[1]>0 else y[1]))(c[int(p)-1],c[int(p)])},[i for i in"".join((r.split()[0]+"1c")*int(r.split()[1]) for r in open(INPUT_FILE).read().split("\n"))],{**{n:(1,1)for n in range(2)},"":set()})[''])
part2 = len(reduce(lambda c,p:{**c,0:(c[0][0]+({"R":1,"L":-1}.get(p,0)),c[0][1]+({"U":1,"D":-1}.get(p,0)))}if p in "RULD" else{**c,"":c[''].union({c[9]})}if p=="c"else{**c,int(p):(lambda x,y:y if abs(x[0]-y[0])<2 and abs(x[1]-y[1])<2 else(y[0]-1 if y[0]-x[0]>0 else y[0]+1 if x[0]-y[0]>0 else y[0],y[1]-1 if y[1]-x[1]>0 else y[1]+1 if x[1]-y[1]>0 else y[1]))(c[int(p)-1],c[int(p)])},[i for i in"".join((r.split()[0]+"123456789c")*int(r.split()[1]) for r in open(INPUT_FILE).read().split("\n"))],{**{n:(1,1)for n in range(10)},"":set()})[''])

print(part1)
print(part2)
