d = [[int(j) if j != '.' else -1 for j in i ] for i in open('10').read().splitlines()]

ny = len(d)
nx = len(d[0])

from functools import cache

@cache
def find_trailhead_from(v,i,j):
  if v == 9:
    return [(i,j)]
  s = []
  if i > 0 and d[i-1][j] == v + 1:
    s += find_trailhead_from(v+1, i-1, j)
  if i < nx - 1 and d[i+1][j] == v + 1:
    s += find_trailhead_from(v+1, i+1, j)
  if j > 0 and d[i][j-1] == v + 1:
    s += find_trailhead_from(v+1, i, j-1)
  if j < ny - 1 and d[i][j+1] == v + 1:
    s += find_trailhead_from(v+1, i, j+1)
  return s

@cache
def find_trailhead_from2(v,i,j):
  if v == 9:
    return 1
  s = 0
  if i > 0 and d[i-1][j] == v + 1:
    s += find_trailhead_from2(v+1, i-1, j)
  if i < nx - 1 and d[i+1][j] == v + 1:
    s += find_trailhead_from2(v+1, i+1, j)
  if j > 0 and d[i][j-1] == v + 1:
    s += find_trailhead_from2(v+1, i, j-1)
  if j < ny - 1 and d[i][j+1] == v + 1:
    s += find_trailhead_from2(v+1, i, j+1)
  return s
  
import tqdm
s = 0
s2 = 0
for i in tqdm.tqdm(range(nx)):
  for j in range(ny):
    if d[i][j] == 0:
      tmp = find_trailhead_from(0,i,j)
      s += len(set(tmp))
      s2 += find_trailhead_from2(0,i,j)
print("s",s,"s2",s2)