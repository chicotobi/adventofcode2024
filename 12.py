from copy import deepcopy

d = [[j for j in i] for i in open('12').read().splitlines()]

ny = len(d)
nx = len(d[0])

def replace_symbol(d, i0, j0):
  queue = [(i0,j0)]
  s_old = d[j0][i0]
  s_new = s_old + '_' + str(i0) + '_' + str(j0)
  d[j0][i0] = s_new
  while len(queue) > 0:
    new_queue = []
    for i,j in queue:
      if i > 0 and d[j][i-1] == s_old:
        d[j][i-1] = s_new
        new_queue.append((i-1,j))
      if i < nx-1 and d[j][i+1] == s_old:
        d[j][i+1] = s_new
        new_queue.append((i+1,j))
      if j > 0 and d[j-1][i] == s_old:
        d[j-1][i] = s_new
        new_queue.append((i,j-1))
      if j < ny-1 and d[j+1][i] == s_old:
        d[j+1][i] = s_new
        new_queue.append((i,j+1))
    queue = deepcopy(new_queue)

# First remap the plant_types to be unique for each region
for i in range(nx):
  for j in range(ny):
    if len(d[j][i]) == 1:
      replace_symbol(d, i, j)
  


plant_types = list(set(j for i in d for j in i))

area = {v:0 for v in plant_types}
area[-1] = 0 
fence = {v:0 for v in plant_types}
fence[-1] = 0

ny = len(d)
nx = len(d[0])

d2 = [[-1]*(nx+2)] + [[-1]+i+[-1] for i in d] + [[-1]*(nx+2)]

# area
for i in d:
  for j in i:
    area[j] += 1

# fence
for i in range(nx+1):
  for j in range(ny+1):
    val_left   = d2[j][i]
    val_right  = d2[j][i+1]
    val_top    = d2[j][i]
    val_bottom = d2[j+1][i]
    
    if val_right != val_left:
      fence[val_right ] += 1
      fence[val_left  ] += 1
    if val_top != val_bottom:
      fence[val_top   ] += 1
      fence[val_bottom] += 1
      
print(sum(area[v] * fence[v] for v in plant_types))