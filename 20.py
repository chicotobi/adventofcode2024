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
dst = [[out[j*nx+i] for i in range(nx)] for j in range(ny)]

# Search cheats
saves = []
for i in range(nx):
  for j in range(ny):
    if d[j][i] == '.':
      dst1 = dst[j][i]
      dst2 = 1e10
      if i > 1 and d[j][i-1] == '#' and d[j][i-2] == '.':
        dst2 = dst[j][i-2]     
        if dst1 - dst2 - 2 > 0:
          saves.append(dst1-dst2-2)   
      if i < nx - 2 and d[j][i+1] == '#' and d[j][i+2] == '.':
        dst2 = dst[j][i+2]
        if dst1 - dst2 - 2 > 0:
          saves.append(dst1-dst2-2)
      if j > 1 and d[j-1][i] == '#' and d[j-2][i] == '.':
        dst2 = dst[j-2][i]
        if dst1 - dst2 - 2 > 0:
          saves.append(dst1-dst2-2)
      if j < ny - 2 and d[j+1][i] == '#' and d[j+2][i] == '.':
        dst2 = dst[j+2][i]
        if dst1 - dst2 - 2 > 0:
          saves.append(dst1-dst2-2)