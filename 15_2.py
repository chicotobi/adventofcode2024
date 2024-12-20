d = open('15').read().splitlines()
idx = [i for i,line in enumerate(d) if line == ''][0]

field = [[j for j in i] for i in d[:idx]]
commands = [j for i in d[idx+1:] for j in i]

# Widen field
field = [[(j,j) if j in ['#','.'] else ('@','.') if j == '@' else ('[',']') for j in i] for i in field]
field = [[k for j in i for k in j] for i in field]

nx = len(field[0])
ny = len(field)
for i in range(nx):
  for j in range(ny):
    if field[j][i] == '@':
      x, y = i, j

def calc_if_pushable(i,j,dire):
  print("called at",i,j,dire)
  # See if the push at this point is possible
  if field[j][i] == '.':
    return True
  if field[j][i] == '#':
    return False
  if dire == '<':
    pushable = calc_if_pushable(i - 1, j, dire)
  elif dire == '>':
    pushable = calc_if_pushable(i + 1, j, dire)
  elif dire == '^':
    if field[j][i] == '[':
      assert(field[j][i+1] == ']')
      pushable1 = calc_if_pushable(i    , j - 1, dire)
      pushable2 = calc_if_pushable(i + 1, j - 1, dire)
      pushable = pushable1 and pushable2
    elif field[j][i] == ']':
      assert(field[j][i-1] == '[')
      pushable1 = calc_if_pushable(i - 1, j - 1, dire)
      pushable2 = calc_if_pushable(i    , j - 1, dire)
      pushable = pushable1 and pushable2
    else:
      pushable = calc_if_pushable(i, j - 1, dire)
  elif dire == 'v':
    if field[j][i] == '[':
      assert(field[j][i+1] == ']')
      pushable1 = calc_if_pushable(i    , j + 1, dire)
      pushable2 = calc_if_pushable(i + 1, j + 1, dire)
      pushable = pushable1 and pushable2
    elif field[j][i] == ']':
      assert(field[j][i-1] == '[')
      pushable1 = calc_if_pushable(i - 1, j + 1, dire)
      pushable2 = calc_if_pushable(i    , j + 1, dire)
      pushable = pushable1 and pushable2
    else:
      pushable = calc_if_pushable(i, j + 1, dire)

  # Return the pushable value
  return pushable


def execute_push_at(i,j,dire):
  # See if the push at this point is possible
  if field[j][i] == '.':
    return
  if field[j][i] == '#':
    return
  if dire == '<':
    execute_push_at(i - 1, j, dire)
  elif dire == '>':
    execute_push_at(i + 1, j, dire)
  elif dire == '^':
    if field[j][i] == '[':
      assert(field[j][i+1] == ']')
      execute_push_at(i    , j - 1, dire)
      execute_push_at(i + 1, j - 1, dire)
    elif field[j][i] == ']':
      assert(field[j][i-1] == '[')
      execute_push_at(i - 1, j - 1, dire)
      execute_push_at(i    , j - 1, dire)
    else:
      execute_push_at(i, j - 1, dire)
  elif dire == 'v':
    if field[j][i] == '[':
      assert(field[j][i+1] == ']')
      execute_push_at(i    , j + 1, dire)
      execute_push_at(i + 1, j + 1, dire)
    elif field[j][i] == ']':
      assert(field[j][i-1] == '[')
      execute_push_at(i - 1, j + 1, dire)
      execute_push_at(i    , j + 1, dire)
    else:
      execute_push_at(i, j + 1, dire)

  if dire == '<':
    field[j][i-1] = field[j][i]
  elif dire == '>':
    field[j][i+1] = field[j][i]
  elif dire == '^':
    if field[j][i] == '[':
      assert(field[j][i+1] == ']')
      field[j-1][i  ] = '['
      field[j-1][i+1] = ']'
      field[j  ][i  ] = '.'
      field[j  ][i+1] = '.'
    elif field[j][i] == ']':
      assert(field[j][i-1] == '[')
      field[j-1][i-1] = '['
      field[j-1][i  ] = ']'
      field[j  ][i-1] = '.'
      field[j  ][i  ] = '.'
    else:
      field[j-1][i] = field[j][i]
  elif dire == 'v':
    if field[j][i] == '[':
      assert(field[j][i+1] == ']')
      field[j+1][i  ] = '['
      field[j+1][i+1] = ']'
      field[j  ][i  ] = '.'
      field[j  ][i+1] = '.'
    elif field[j][i] == ']':
      assert(field[j][i-1] == '[')
      field[j+1][i-1] = '['
      field[j+1][i  ] = ']'
      field[j  ][i-1] = '.'
      field[j  ][i  ] = '.'
    else:
      field[j+1][i] = field[j][i]

for c in commands:     
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
    
  val = calc_if_pushable(x, y, c)
  print("command",c,"pushable",val)
  if val:
    execute_push_at(x, y, c)
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
    if field[j][i] == '[':
      s += 100 * j + i
print(s)