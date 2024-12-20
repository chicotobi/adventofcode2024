d = open('17').read().splitlines()
a = int(d[0].split(" ")[-1])
b = int(d[1].split(" ")[-1])
c = int(d[2].split(" ")[-1])
prog = [int(i) for i in d[4].split(" ")[1].split(",")]

ptr = 0
out = []
while ptr < len(prog):
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
print(','.join(str(i) for i in out))
