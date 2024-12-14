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
fence_segments = {v:[] for v in plant_types}
fence_segments[-1] = []

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
      fence_segments[val_right ] += [[(i+1,j),(i+1,j+1)]]
      fence_segments[val_left  ] += [[(i+1,j),(i+1,j+1)]]
    if val_top != val_bottom:
      fence_segments[val_top   ] += [[(i,j+1),(i+1,j+1)]]
      fence_segments[val_bottom] += [[(i,j+1),(i+1,j+1)]]

fence_posts = {k:list(set(j for i in x for j in i)) for k, x in fence_segments.items()}

# Now for each fence find th
fence_corners = dict()
fence_corners[-1] = 0
for v in plant_types:
  # Count the corners - is equal to the number of straight lines
  # Edge case: Figure-Eight-Fence
  corners = []
  for i,j in fence_posts[v]:    
    if [(i-1,j),(i,j)] in fence_segments[v] and [(i,j),(i+1,j)] in fence_segments[v]:
      if [(i,j-1),(i,j)] in fence_segments[v] and [(i,j),(i,j+1)] in fence_segments[v]:
        # Edge case: Figure-Eight-Fence, count the pole twice as a corner
        corners += [(i,j), (i,j)]
      else:
        # Horizontal but not vertical - don't count
        continue
    else:
      if [(i,j-1),(i,j)] in fence_segments[v] and [(i,j),(i,j+1)] in fence_segments[v]:
        # Vertical but not horizontal - don't count
        continue
      else:
        # Neither horizontal nor vertical - count once
        corners += [(i,j)]
  fence_corners[v] = corners
 
print(sum(area[v] * len(fence_corners[v]) for v in plant_types))