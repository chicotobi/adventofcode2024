def nxt(x):
  x = (x ^ (x *  64)) % (2**24)
  x = (x ^ (x // 32)) % (2**24)
  x = (x ^ (x * 2048)) % (2**24)
  return x

d = open('22').read().splitlines()

prices = []
dct = {}
for i in d:
  dct[i] = {}
  x = int(i)
  tmp = [x%10]
  chg = []
  for j in range(2000):
    oldx = x
    x = nxt(x)
    tmp.append(x%10)
    chg.append(tmp[-1]-tmp[-2])
    if len(chg) >= 4:
      sq = tuple(chg[-4:])
      if sq not in dct[i].keys():
        dct[i][sq] = x%10
        
  prices.append(tmp)

value_of_sq = {}
for v in dct.values():
  for sq, val in v.items():
    if sq not in value_of_sq.keys():
      value_of_sq[sq] = 0
    value_of_sq[sq] += val
    
max_val = max(value_of_sq.values())

print(max_val)