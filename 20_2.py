from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import shortest_path

d = [[j for j in i] for i in open('20').read().splitlines()]

nx = len(d[0])
ny = len(d)

for i in range(nx):
  for j in range(ny):
    if d[j][i] == 'S':
      sx, sy = i, j
      sidx = sy * nx + sx
      d[j][i] = '.'
    if d[j][i] == 'E':
      ex, ey = i, j
      eidx = ey * nx + ex
      d[j][i] = '.'

mat_i = []
mat_j = []
mat_v = []
for i in range(nx):
  for j in range(ny):
    if d[j][i] == '.':
      idx1 = j * nx + i
      if i > 0 and d[j][i-1] == '.':
        idx2 = j * nx + i - 1
        mat_i.append(idx1)
        mat_j.append(idx2)
        mat_v.append(1)
      if i < nx - 1 and d[j][i+1] == '.':
        idx2 = j * nx + i + 1
        mat_i.append(idx1)
        mat_j.append(idx2)
        mat_v.append(1)
      if j > 0 and d[j-1][i] == '.':
        idx2 = (j-1) * nx + i
        mat_i.append(idx1)
        mat_j.append(idx2)
        mat_v.append(1)
      if j < ny - 1 and d[j+1][i] == '.':
        idx2 = (j+1) * nx + i
        mat_i.append(idx1)
        mat_j.append(idx2)
        mat_v.append(1)
        
mat = coo_matrix((mat_v,(mat_i,mat_j)),shape = (nx*ny,nx*ny))

out = shortest_path(mat, indices = eidx)
#dst = [[int(out[j*nx+i]) if out[j*nx+i] < 1e10 else In for i in range(nx)] for j in range(ny)]
dst = [[out[j*nx+i] for i in range(nx)] for j in range(ny)]

# Search cheats with up to 20 picoseconds
cheats = []
max_cheat_length = 20
min_saved_length = 100
import tqdm
for i in tqdm.tqdm(range(nx)):
  for j in range(ny):
    if d[j][i] == '.':
      dst1 = dst[j][i]
      dst2 = 1e10
      for di in range(- max_cheat_length, max_cheat_length + 1):
        if 0 <= i+di and i+di <= nx - 1:
          for dj in range(- max_cheat_length, max_cheat_length + 1):
            if 0 <= j+dj and j+dj <= ny - 1:
              if 1 < abs(di)+abs(dj) and abs(di)+abs(dj) <= max_cheat_length:
                if d[j+dj][i+di] == '.':
                  dst2 = dst[j+dj][i+di]
                  saved_length = dst1 - dst2 - abs(di) - abs(dj)
                  if saved_length >= min_saved_length:   
                    cheats.append(saved_length)
                    
from collections import Counter, OrderedDict

ctr = Counter(cheats)
od = OrderedDict(sorted(ctr.items()))
for k,v in od.items():
  print(f"There are {v} cheats that save {k} picoseconds")
  
# Solution
print(len(cheats))