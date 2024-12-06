import tqdm
from copy import deepcopy

dorig = open('6').read().splitlines()
dorig = [[j for j in l] for l in dorig]
ny = len(dorig[0])
nx = len(dorig)

# 0 up 1 right 2 down 3 left
y, x = [(i,j) for i, l in enumerate(dorig) for j, c in enumerate(l) if c == '^'][0]
dire = 0
dorig[y][x] = '.'
  
def walk(d, x, y, dire, path):
  while True:
    # Detect loop
    if (x, y, dire) in path:
      return 1, path
    
    path += [(x,y,dire)]
    
    # At the boundary
    if (dire, y) in [(0, 0), (2, ny-1)] or (dire, x) in [(1, nx-1), (3, 0)]:
      return 0, path
    
    # Advance if possible
    if dire == 0:
      if y == 0:
        return 0, path
      if d[y-1][x] == '.':
        y -= 1
        continue
    elif dire == 1:
      if x == nx - 1:
        return 0, path
      if d[y][x+1] == '.':
        x += 1
        continue
    elif dire == 2:
      if y == ny - 1:
        return 0, path
      if d[y+1][x] == '.':
        y += 1
        continue
    elif dire == 3:
      if x == 0:
        return 0, path
      if d[y][x-1] == '.':
        x -= 1
        continue
        
    # Turn if needed
    if dire == 0 and d[y-1][x] == '#':
      dire = (dire+1)%4
    elif dire == 1 and d[y][x+1] == '#':
      dire = (dire+1)%4
    elif dire == 2 and d[y+1][x] == '#':
      dire = (dire+1)%4
    elif dire == 3 and d[y][x-1] == '#':
      dire = (dire+1)%4
  
result, path = walk(dorig, x, y, dire, [])

# Simplify path
locations = list(set((x,y) for (x,y,_) in path))
len_locations = len(locations)
print(len_locations)

# Try with putting obstacles at the defined locations
loops = 0
for obx, oby in tqdm.tqdm(locations):
  d2 = deepcopy(dorig)
  d2[oby][obx] = '#'
  tmp, _ = walk(d2, x, y, dire, [])
  loops += tmp
print(loops)