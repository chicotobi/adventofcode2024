from numpy import std

#d = open('14_test').read().splitlines()
#nx, ny = 11, 7

d = open('14').read().splitlines()
nx, ny = 101, 103

t = 100

# Load robots
d2 = []
for r in d:
  loc, vel = r.split(' ')
  
  x, y = loc.split("=")[1].split(',')
  x = int(x)
  y = int(y)
  
  vx, vy = vel.split("=")[1].split(',')
  vx = int(vx)
  vy = int(vy)
  d2.append([x,y,vx,vy])
  
t = 0
while True:
  t += 1
  for i in range(len(d2)):
    x,y,vx,vy = d2[i]
    d2[i] = (x+vx)%nx, (y+vy)%ny, vx, vy

  arr = [[0]*nx for i in range(ny)]
  
  q1 = q2 = q3 = q4 = 0
  xmid = nx // 2
  ymid = ny // 2
  for i in range(len(d2)):
    x,y,_,_ = d2[i]
    arr[y][x] += 1
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
  
  danger_level = q1*q2*q3*q4
  sdx = std(list(i[0] for i in d2))
  sdy = std(list(i[1] for i in d2))
  if max(max(i) for i in arr) == 1:
  # if sdx < 25 and sdy < 25:
  # if danger_level < 5e7:
    s = '\n'.join(''.join(str(j) for j in i) for i in arr).replace('0','.')
    print(s)
    print("danger level",danger_level)
    print("sd x",sdx,"sd y",sdy)
    print("time:",t)
    break