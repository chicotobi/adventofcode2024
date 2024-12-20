from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import shortest_path

def pr(d0):
  field = [['.' for j in range(nx)] for i in range(ny)]
  for x,y in d0:
    field[y][x] = '#'
  print('\n'.join(''.join(i) for i in field))

# Test
d = [tuple(int(j) for j in i.split(',')) for i in open('18_test').read().splitlines()]
nx = ny = 7
n = 12

# Real
d = [tuple(int(j) for j in i.split(',')) for i in open('18').read().splitlines()]
nx = ny = 71
n = 1024

# Solve
start_idx = 0 * nx + 0
end_idx = nx * ny - 1

d = d[:n]

mat_i = []
mat_j = []
mat_v = []
for i in range(nx):
  for j in range(ny):
    idx = i * ny + j
    if (i,j) not in d:
      if i > 0 and (i-1,j) not in d:
        idx2 = (i-1) * ny + j
        mat_i.append(idx)
        mat_j.append(idx2)
        mat_v.append(1)
      if i < nx - 1 and (i+1,j) not in d:
        idx2 = (i+1) * ny + j
        mat_i.append(idx)
        mat_j.append(idx2)
        mat_v.append(1)
      if j > 0 and (i,j-1) not in d:
        idx2 = i * ny + j - 1
        mat_i.append(idx)
        mat_j.append(idx2)
        mat_v.append(1)
      if j < ny - 1 and (i,j+1) not in d:
        idx2 = i * ny + j + 1
        mat_i.append(idx)
        mat_j.append(idx2)
        mat_v.append(1)

mat = coo_matrix((mat_v,(mat_i, mat_j)), shape = (nx*ny,nx*ny))

out, pre = shortest_path(mat, indices = start_idx, return_predecessors = True)
min_dst = out[end_idx]
print("min_dst",min_dst)