d = open('15').read().splitlines()
idx = [i for i,line in enumerate(d) if line == ''][0]

field = [[j for j in i] for i in d[:idx]]
commands = [j for i in d[idx+1:] for j in i]

nx = len(field[0])
ny = len(field)
for i in range(nx):
  for j in range(ny):
    if field[j][i] == '@':
      x, y = i, j
 
for c in commands:
  # Get the next direction
  if c == '<':
    vx, vy = [-1, 0]
  elif c == '>':
    vx, vy = [ 1, 0]
  elif c == '^':
    vx, vy = [0, -1]
  elif c == 'v':
    vx, vy = [0,  1]
  else:
    raise
  print("c",c)
  
  # Calculate how far the blocks can be pushed in this direction
  xn = x
  yn = y
  step_width = 1
  success = True
  while True:
    xn += vx
    yn += vy
    if 0 > xn or xn > nx - 1 or 0 > yn or yn > ny - 1 or field[yn][xn] == '#':
      step_width = 0
      print("no push possible")
      break
    if field[yn][xn] == '.':
      print('found free field')
      break
    print("incr")
    step_width += 1
  print("step_width",step_width)
    
  # Push the blocks (including player)
  for i in range(step_width, 0, -1):
    xto   = x +  i      * vx
    yto   = y +  i      * vy
    xfrom = x + (i - 1) * vx
    yfrom = y + (i - 1) * vy
    field[yto][xto] = field[yfrom][xfrom]
  if step_width > 0:
    field[y][x] = '.'
    x += vx
    y += vy
  
  # Print the field
  print('\n'.join(''.join(i) for i in field))
  #input()
  
# Calc sum of GPS coords
s = 0
for i in range(nx):
  for j in range(ny):
    if field[j][i] == 'O':
      s += 100 * j + i
print(s)