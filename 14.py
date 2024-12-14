#d = open('14_test').read().splitlines()
#nx, ny = 11, 7

d = open('14').read().splitlines()
nx, ny = 101, 103

t = 100

# Predict robots
q1 = q2 = q3 = q4 = 0
for r in d:
  loc, vel = r.split(' ')
  
  x, y = loc.split("=")[1].split(',')
  x = int(x)
  y = int(y)
  
  vx, vy = vel.split("=")[1].split(',')
  vx = int(vx)
  vy = int(vy)
  
  x = (x + t * vx) % nx
  y = (y + t * vy) % ny
  
  print(x,y)
  xmid = nx // 2
  ymid = ny // 2
  if x < xmid:
    if y < ymid:
      q1 += 1
    elif y > ymid:
      q2 += 1
  elif x > xmid:
    if y < ymid:
      q3 += 1
    elif y > ymid:
      q4 += 1
print(q1,q2,q3,q4,q1*q2*q3*q4)