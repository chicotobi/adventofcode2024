from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import shortest_path
import tqdm

d = [[j for j in i] for i in open('16_test').read().splitlines()]

# dire 0 1 2 3
# up right down left

ny = len(d)
nx = len(d[0])

for i in range(nx):
  for j in range(ny):
    if d[j][i] == 'S':
      sx, sy = i, j
    if d[j][i] == 'E':
      ex, ey = i, j
sdire = 1

def pr(field):
  s = '\n'.join(''.join(i) for i in field)
  print(s)

# Create a graph
nodes = []
for i in range(nx):
  for j in range(ny):
    if d[j][i] in ['S','E','.']:
      for dire in range(4):
        nodes.append((i,j,dire))
nodes_dct = {k:v for v, k in enumerate(nodes)}
nodes_set = set(nodes)

mat_i = []
mat_j = []
mat_v = []
for i in tqdm.tqdm(range(nx)):
  for j in range(ny):
    
    # Add the direction changes - expensive
    for dir0 in range(4):
      for dir1 in range(4):
        if dir0 != dir1:
          if (i,j,dir0) in nodes_set and (i,j,dir1) in nodes_set:
            mat_i.append(nodes_dct[(i,j,dir0)])
            mat_j.append(nodes_dct[(i,j,dir1)])
            mat_v.append(1000)
    
    # Add a straight ahead walk - cheap
    if (i,j,1) in nodes_set and (i+1, j, 1) in nodes_set:
      mat_i.append(nodes_dct[(i  ,j,1)])
      mat_j.append(nodes_dct[(i+1,j,1)])
      mat_v.append(1)
    if (i,j,3) in nodes_set and (i-1, j, 3) in nodes_set:
      mat_i.append(nodes_dct[(i  ,j,3)])
      mat_j.append(nodes_dct[(i-1,j,3)])
      mat_v.append(1)
    if (i,j,2) in nodes_set and (i, j+1, 2) in nodes_set:
      mat_i.append(nodes_dct[(i,j  ,2)])
      mat_j.append(nodes_dct[(i,j+1,2)])
      mat_v.append(1)
    if (i,j,0) in nodes_set and (i, j-1, 0) in nodes_set:
      mat_i.append(nodes_dct[(i,j  ,0)])
      mat_j.append(nodes_dct[(i,j-1,0)])
      mat_v.append(1)
mat = coo_matrix((mat_v,(mat_i, mat_j)))

start_idx = nodes_dct[(sx,sy,sdire)]
end_idxs = [nodes_dct[(ex,ey,i)] for i in range(4)]

out = shortest_path(mat, indices = start_idx)
min_dst = min(out[i] for i in end_idxs)
print("min_dst",min_dst)
    