def pr(prog):
  print("prog:",prog)
  for i in range(len(prog)//2):
    opcode = prog[2 * i]
    literal = prog[2 * i + 1]
    
    if literal in [0,1,2,3]:
      combo = str(literal)
    elif literal == 4:
      combo = 'rega'
    elif literal == 5:
      combo = 'regb'
    elif literal == 6:
      combo = 'regc'
      
    if opcode == 0:
      cmd = 'adv ' + 'rega = rega // 2 ** ' + combo
    elif opcode == 1:
      cmd = 'bxl ' + 'regb = regb xor ' + str(literal)
    elif opcode == 2:
      cmd = 'bst ' + 'regb = ' + combo + ' % 8'
    elif opcode == 3:
      cmd = 'jnz ' + 'if a != 0: jmp to program jmp to ' + str(literal)
    elif opcode == 4:
      cmd = 'bxc ' + 'regb = regb xor regc'
    elif opcode == 5:
      cmd = 'out ' + 'write ' + combo + ' % 8'
    elif opcode == 6:
      cmd = 'bdv ' + 'regb = rega // 2 ** ' + combo
    elif opcode == 7:
      cmd = 'cdv ' + 'regc = rega // 2 ** ' + combo
    print(cmd)

def exec_with_a(a):
  d = open('17').read().splitlines()
  b = int(d[1].split(" ")[-1])
  c = int(d[2].split(" ")[-1])
  prog = [int(i) for i in d[4].split(" ")[1].split(",")]
  
  #pr(prog)  
  
  ptr = 0
  out = []
  while ptr < len(prog):
    print("a",a,"b",b,"c",c)
    opcode = prog[ptr]
    literal = prog[ptr+1]
    if literal in [0,1,2,3]:
      combo = literal
    elif literal == 4:
      combo = a
    elif literal == 5:
      combo = b
    elif literal == 6:
      combo = c
      
    if opcode == 0: # adv
      a = a // (2 ** combo)
    elif opcode == 1: # bxl
      b = b ^ literal
    elif opcode == 2: # bst
      b = combo % 8
    elif opcode == 3: # jnz
      if a != 0:
        ptr = literal
        continue
    elif opcode == 4: # bxc
      b = b ^ c
    elif opcode == 5: # out
      out.append(combo%8)
    elif opcode == 6: # bdv
      b = a // (2 ** combo)
    elif opcode == 7: # cdv
      c = a // (2 ** combo)
    ptr += 2
  return out


def to_oct(x):
  s = ''
  while x > 0:
    s = str(x % 8) + s
    x = x // 8
  return s

def from_oct(s):
  x = 0
  while len(s) > 0:
    x *= 8
    x = x + int(s[0])
    s = s[1:]
  return x


a0 = 0
a1 = 281474976710656

n = 10000
step = (a1-a0) // n

prog = [2, 4, 1, 3, 7, 5, 0, 3, 4, 1, 1, 5, 5, 5, 3, 0]
for a in range(a0, a1, step):
  out = exec_with_a(a)
  score = 0  
  diff = [i-j for i,j in zip(out[::-1],prog[::-1])]
  for i in diff:
    if i == 0:
      score += 1
    else:
      break
  if score > 3:
    print(to_oct(a),a,score,diff)