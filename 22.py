def nxt(x):
  x = (x ^ (x *  64)) % (2**24)
  x = (x ^ (x // 32)) % (2**24)
  x = (x ^ (x * 2048)) % (2**24)
  return x

d = open('22').read().splitlines()

s = 0
for i in d:
  x = int(i)
  for j in range(2000):
    x = nxt(x)
  s += x
print(s)