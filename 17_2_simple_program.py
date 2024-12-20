import random

def to_oct(x):
  s = []
  while x > 0:
    s = s + [x % 8]
    x = x // 8
  missing_zeros = [0] * (16-len(s))
  return missing_zeros + s[::-1]

def from_oct(s):
  x = 0
  while len(s) > 0:
    x *= 8
    x = x + int(s[0])
    s = s[1:]
  return x

def to_bin(x):
  s = []
  while x > 0:
    s = s + [x % 2]
    x = x // 2
  missing_zeros = [0] * (48-len(s))
  return missing_zeros + s[::-1]

def from_bin(s):
  x = 0
  while len(s) > 0:
    x *= 2
    x = x + int(s[0])
    s = s[1:]
  return x

def exec_with_a(a):
  b = c = 0  
  v = []
  while a > 0:
    c = a // 2 ** ((3 - a) % 8)
    b = (a % 8) ^ c ^ 6
    a = a // 8
    v.append(b%8)
  return v


while True:
  #s = [random.randint(0, 7) for i in range(16)]
     
  s = to_bin(random.getrandbits(48))
  s[0] = 1
  s[1] = 1
  s[2] = 0
  
  s[4] = 0
  s[5] = 1
  
  
  if s[7] == s[8]:
    continue
  
  s[9] = 0
  if s[10] == s[11]:
    continue
  
  s[38] = 1
  
  s[39] = 0
  
  s[42] = 1
  s[44] = 1
  
  s[45] = 1
  s[47] = 1
  
  if s[40] == s[41]:
    continue
  
  if s[43] != s[46]:
    continue
  
  a0 = from_bin(s)  
  v = exec_with_a(a0)
  starts_with = [2,4,1,3,7,5]
  ends_with = [1,1,5,5,5,3,0]
  if v[16-len(ends_with):] == ends_with:
    if v[:len(starts_with)] == starts_with:
      # tmp = ''.join(str(i) for i in to_oct(a0))
      tmp0 = [str(i) for i in to_bin(a0)]
      tmp = ' '.join(''.join(tmp0[3*i:3*i+3]) for i in range(16))
      print(tmp, v)

# prog 2,4, 1,3, 7,5, 0,3, 4,1, 1,5, 5,5, 3,0

# [1, 5, 0, 5, 2, 0, 1, 3, 5]
#exec_with_a(45483412)