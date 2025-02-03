d = open('25').read().splitlines()

n = (len(d) + 1) // 8

keys = []
locks = []
for i in range(n):
  tmp = d[8*i:8*i+7]
  if tmp[6][0] == '#':
    key = []
    for j in range(5):
      l = 6
      while tmp[6-l][j] == '.':
        l -= 1
      key.append(l)
    keys.append(key)
  elif tmp[0][0] == '#':
    typ = 'lock'
    lock = []
    for j in range(5):
      l = 0
      while tmp[l+1][j] != '.':
        l += 1
      lock.append(l)
    locks.append(lock)
  else:
    raise
    
s = 0
for k in keys:
  for l in locks:
    if max(i+j for i,j in zip(k,l)) <= 5:
      s += 1
print(s)