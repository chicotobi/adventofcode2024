d = open('24').read().splitlines()

idx = [i for i,x in enumerate(d) if x == ''][0]

vals = [i.split(":") for i in d[:idx]]
vals = {i:int(j) for i,j in vals}

rules = [i.split(" -> ") for i in d[idx+1:]]
rules = [i.split(" ")+ [j] for i,j in rules]
applied = [False] * len(rules)

while not all(applied):
  for idx, (in1, op, in2, out) in enumerate(rules):
    if not applied[idx]:
      if in1 in vals.keys() and in2 in vals.keys():
        if op == 'AND':
          vals[out] = vals[in1] and vals[in2]
        elif op == 'OR':
          vals[out] = vals[in1] or vals[in2]
        elif op == 'XOR':
          vals[out] = vals[in1] ^ vals[in2]
        applied[idx] = True
      

# Extract solution
import collections
vals2 = collections.OrderedDict(sorted(vals.items()))

s = 0
vals3 = [v for k,v in vals2.items() if 'z' in k][::-1]
for v in vals3:
  s *= 2
  s += v
print(s)