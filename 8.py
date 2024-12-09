d = open('8').read().splitlines()

chars = list(set(j for i in d for j in i))

ny = len(d)
nx = len(d[0])

antinodes = []
for char in chars:
  if char == '.':
    continue
  locs = [(i,j) for i,l in enumerate(d) for j,c in enumerate(l) if c == char]
  locs = list(set(locs))
  #iterate through locs
  for i in range(len(locs)):
    for j in range(i+1, len(locs)):
      x1, y1 = locs[i]
      x2, y2 = locs[j]
          
      # Run in one direction
      vecx, vecy = (x2-x1, y2-y1)
      ax, ay = x1, y1
      while True:
        ax, ay = ax + vecx, ay + vecy
        if 0 <= ax and ax < nx and 0 <= ay and ay < ny:
          antinodes += [(ax,ay)]
        else:
          break
        
      # Run in other direction
      vecx, vecy = (x1-x2, y1-y2)
      ax, ay = x2, y2
      while True:
        ax, ay = ax + vecx, ay + vecy
        if 0 <= ax and ax < nx and 0 <= ay and ay < ny:
          antinodes += [(ax,ay)]
        else:
          break
        
antinodes = list(set(antinodes))
print(len(antinodes))  