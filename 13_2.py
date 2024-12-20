from math import gcd

d = open('13').read().splitlines()
  
s = 0
for i in range(len(d)//4+1):
  ax = int(d[4*i].split(' ')[2].split('+')[1].split(',')[0])
  ay = int(d[4*i].split(' ')[3].split('+')[1])
  bx = int(d[4*i+1].split(' ')[2].split('+')[1].split(',')[0])
  by = int(d[4*i+1].split(' ')[3].split('+')[1])
  x  = int(d[4*i+2].split(' ')[1].split('=')[1].split(',')[0])
  y  = int(d[4*i+2].split(' ')[2].split('=')[1])
  
  x += 10000000000000
  y += 10000000000000
  print()
  print(ax,ay,bx,by,x,y)
  
  a = (x * by - y * bx) / (ax * by - ay * bx)
  b = (ax * y - ay * x) / (ax * by - ay * bx)
  print(a,b)
  if abs(round(a)-a) < 1e-3 and abs(round(b)-b) < 1e-3:
    print("works")
    s += 3 * round(a) + round(b)
      
print("s",s)