from copy import deepcopy
import tqdm

def calc(x, val):
  if x[0] > val:
    return False
  if len(x) == 1:
    #print(x[0],val)
    #print(x[0] == val)
    return x[0] == val
  
  # Try add
  x1 = deepcopy(x)
  x1[1] *= x1[0]
  del x1[0]
  r1 = calc(x1, val)
  
  # Try add
  x2 = deepcopy(x)
  x2[1] += x2[0]
  del x2[0]
  r2 = calc(x2, val)
  
  # Try concat()
  x3 = deepcopy(x)
  x3[1] = int(str(x3[0]) + str(x3[1]))
  del x3[0]
  r3 = calc(x3, val)
  
  #print(r1,r2)
  return r1 or r2 or r3

d = open('7').read().splitlines()

s = 0
for i in tqdm.tqdm(d):
  val, x = i.split(':')
  val = int(val)
  x = [int(i) for i in x.split()]
  if calc(x, val):
    #print(val)
    s += val
print(s)