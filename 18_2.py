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

# Real
d = [tuple(int(j) for j in i.split(',')) for i in open('18').read().splitlines()]
nx = ny = 71

# Solve
start_idx = 0 * nx + 0
end_idx = nx * ny - 1

edges = []
for i in range(nx):
  for j in range(ny):
    idx = i * ny + j
    
    if i > 0:
      idx2 = (i-1) * ny + j
      edges.append((idx,idx2,1))
    
    if i < nx - 1:
      idx2 = (i+1) * ny + j
      edges.append((idx,idx2,1))
    
    if j > 0:
      idx2 = i * ny + j - 1
      edges.append((idx,idx2,1))
    
    if j < ny - 1:
      idx2 = i * ny + j + 1
      edges.append((idx,idx2,1))

min_dst = 0
k = -1
while min_dst < 1e10:
  k += 1
  # Remove edges for 
  x0, y0 = d[k]
  idx = x0 * ny + y0
  edges = [(i,j,v) for (i,j,v) in edges if i != idx and j != idx]
  
  mat_i = [i for i,j,v in edges]
  mat_j = [j for i,j,v in edges]
  mat_v = [v for i,j,v in edges]
  mat = coo_matrix((mat_v,(mat_i, mat_j)), shape = (nx*ny,nx*ny))
  out, pre = shortest_path(mat, indices = start_idx, return_predecessors = True)
  min_dst = out[end_idx]
  print("k",k,"min_dst",min_dst)
print("node",d[k])