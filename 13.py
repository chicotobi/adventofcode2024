d = open('13').read().splitlines()

s = 0
for i in range(len(d)//4+1):
  ax = int(d[4*i].split(' ')[2].split('+')[1].split(',')[0])
  ay = int(d[4*i].split(' ')[3].split('+')[1])
  bx = int(d[4*i+1].split(' ')[2].split('+')[1].split(',')[0])
  by = int(d[4*i+1].split(' ')[3].split('+')[1])
  x  = int(d[4*i+2].split(' ')[1].split('=')[1].split(',')[0])
  y  = int(d[4*i+2].split(' ')[2].split('=')[1])
  print(ax,ay,bx,by,x,y)
  
  
  m = 100
  min_cost = 1e100
  for a in range(m+1):
    if x // bx * bx == x and y // by * by == y:
      b1 = x // bx
      b2 = y // by
      if b1 == b2:
        cost = 3 * a + b1
        min_cost = min(min_cost, cost)
    x -= ax
    y -= ay
  if min_cost < 1e100:
    s += cost
    
print(s)