d = open('4').read().splitlines()
  
def check(c1,c2,c3,c4):
  return (c1=='X' and c2=='M' and c3 == 'A' and c4 == 'S')

def check2(m1,m2,a,s1,s2):
  return m1 == 'M' and m2 == 'M' and a == 'A' and s1 == 'S' and s2 == 'S'

s = 0
ny = len(d)
nx = len(d[0])
for i in range(nx):
  for j in range(ny):
    # Down
    if j + 3 < ny:
      s += check(d[i][j],d[i][j+1],d[i][j+2],d[i][j+3])      
    # Up
    if j - 3 >= 0:
      s += check(d[i][j],d[i][j- 1],d[i][j-2],d[i][j-3])     
    # Right
    if i + 3 < nx:
      s += check(d[i][j],d[i+1][j],d[i+2][j],d[i+3][j])      
    # Left
    if i - 3 >= 0:
      s += check(d[i][j],d[i-1][j],d[i-2][j],d[i-3][j])      
    
    # Down right
    if i + 3 < nx and j + 3 < ny:
      s += check(d[i][j],d[i+1][j+1],d[i+2][j+2],d[i+3][j+3])      
      
    # Down left
    if i - 3 >= 0 and j + 3 < ny:
      s += check(d[i][j],d[i-1][j+1],d[i-2][j+2],d[i-3][j+3])      
      
    # Up right
    if i + 3 < nx and j - 3 >= 0:
      s += check(d[i][j],d[i+1][j-1],d[i+2][j-2],d[i+3][j-3])      
      
    # Up left
    if i - 3 >= 0 and j - 3 >= 0:
      s += check(d[i][j],d[i-1][j-1],d[i-2][j-2],d[i-3][j-3])      
      
print(s)


s = 0
ny = len(d)
nx = len(d[0])
for i in range(nx-2):
  for j in range(ny-2):
    # 1.2
    # .3.
    # 4.5
    c1 = d[i][j]
    c2 = d[i+2][j]
    c3 = d[i+1][j+1]
    c4 = d[i][j+2]
    c5 = d[i+2][j+2]
    
    # Down
    s += check2(c1,c2,c3,c4,c5)
    
    # Up
    s += check2(c4,c5,c3,c1,c2)
    
    # Right
    s += check2(c1,c4,c3,c2,c5)
    
    # Left
    s += check2(c2,c5,c3,c1,c4)
    
      
print(s)