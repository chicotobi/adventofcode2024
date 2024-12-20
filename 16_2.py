from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import shortest_path
import tqdm

d = [[j for j in i] for i in open('16').read().splitlines()]

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
  print()
  s = '\n'.join(''.join(i) for i in field)
  print(s)

# First detect all nodes in the graph
nodes = []
for i in range(nx):
  for j in range(ny):
    # Is this location a node, i.e. start, end, or crossing
    if d[j][i] in ['S','E']:
      for dire in range(4):
        nodes += [(i,j,dire)]
      d[j][i] = 'O'
    elif d[j][i] == '.':
      # Check if it's a crossing
      n = 0
      n += (i > 0      and d[j  ][i-1] == '.')
      n += (i < nx - 1 and d[j  ][i+1] == '.')
      n += (j > 0      and d[j-1][i  ] == '.')
      n += (j < ny - 1 and d[j+1][i  ] == '.')
      if n >= 3:
        for dire in range(4):
          nodes += [(i,j,dire)]
        d[j][i] = 'O'
nodes_dct = {node:idx for idx, node in enumerate(nodes)}


edges = []

def find_next_node(i0, j0, dire0):
  global edges
    
  idx0 = nodes_dct[(i0,j0,dire0)]
  
  cost = 1
  i, j, dire = i0, j0, dire0
  
  i += 1 * (dire == 1) - 1 * (dire == 3)
  j += 1 * (dire == 2) - 1 * (dire == 0)   
  
  while d[j][i] != 'O':      
    if dire != 1 and i > 0 and d[j][i-1] != '#':
      cost += 1 + (dire != 3) * 1000
      i -= 1
      dire = 3
    elif dire != 3 and i < nx-1 and d[j][i+1] != '#':
      cost += 1 + (dire != 1) * 1000
      i += 1
      dire = 1
    elif dire != 2 and j > 0 and d[j-1][i] != '#':
      cost += 1 + (dire != 0) * 1000
      j -= 1
      dire = 0
    elif dire != 0 and j < ny-1 and d[j+1][i] != '#':
      cost += 1 + (dire != 2) * 1000
      j += 1
      dire = 2
    else:
      # dead end, no node, return without a new edge
      return
  idx = nodes_dct[(i,j,dire)]
  edges += [(idx0, idx, cost)]

# Now find all edges from node to node 
for idx1, (i, j, dire) in tqdm.tqdm(enumerate(nodes)):
  if i > 0      and d[j][i-1] == '.' and dire == 3:
    find_next_node(i, j, 3)
  if i < nx - 1 and d[j][i+1] == '.' and dire == 1:
    find_next_node(i, j, 1)
  if j > 0      and d[j-1][i] == '.' and dire == 0:
    find_next_node(i, j, 0)
  if j < ny - 1 and d[j+1][i] == '.' and dire == 2:
    find_next_node(i, j, 2)

# Now add edges for turning at nodes
for i in range(nx):
  for j in range(ny):
    if (i,j,0) in nodes:
      for dir0 in range(4):
        for dir1 in range(4):
          # Turning 90 degrees
          if abs(dir0-dir1) == 1 or abs(dir0-dir1) == 3:
            idx1 = nodes_dct[(i,j,dir0)]
            idx2 = nodes_dct[(i,j,dir1)]
            edges += [(idx1,idx2,1000)]

mat_i = [i for i,j,v in edges]
mat_j = [j for i,j,v in edges]
mat_v = [v for i,j,v in edges]
mat = coo_matrix((mat_v,(mat_i, mat_j)))

start_idx = nodes_dct[(sx,sy,sdire)]
end_idxs = [nodes_dct[(ex,ey,dire)] for dire in range(4)]

out = shortest_path(mat, indices = start_idx)
min_dst = min(out[i] for i in end_idxs)
print()
print("min_dst",min_dst)
    

import networkx as ntx

pathes = []
G = ntx.DiGraph()
G.add_weighted_edges_from(edges)
for i in range(4):
  all_shortest_paths = list(ntx.all_shortest_paths(G, source=start_idx, target=end_idxs[i], weight='weight')) 
  for path in all_shortest_paths:
      weight = sum(G[u][v]['weight'] for u, v in zip(path[:-1], path[1:]))
      if weight == min_dst:
        pathes.append(path)
  
# Now count the fields these pathes touch
touched_locs = set()
for path in pathes:
  for k in range(len(path)-1):
    i, j, dire = nodes[path[k]]
    i1, j1, dire1 = nodes[path[k+1]]
    touched_locs.add((i,j))
    touched_locs.add((i1,j1))
    if (i,j) != (i1,j1):
      i += 1 * (dire == 1) - 1 * (dire == 3)
      j += 1 * (dire == 2) - 1 * (dire == 0)   
      touched_locs.add((i,j))
      while (i,j) != (i1,j1): 
        touched_locs.add((i,j))
        if dire != 1 and i > 0 and d[j][i-1] != '#':
          i -= 1
          dire = 3
        elif dire != 3 and i < nx-1 and d[j][i+1] != '#':
          i += 1
          dire = 1
        elif dire != 2 and j > 0 and d[j-1][i] != '#':
          j -= 1
          dire = 0
        elif dire != 0 and j < ny-1 and d[j+1][i] != '#':
          j += 1
          dire = 2
        #input()
print("touched_locs",len(touched_locs))