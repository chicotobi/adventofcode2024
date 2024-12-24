coords1 = {
  '0': (1,0),
  'A': (2,0),
  '1': (0,1),
  '2': (1,1),
  '3': (2,1),
  '4': (0,2),
  '5': (1,2),
  '6': (2,2),
  '7': (0,3),
  '8': (1,3),
  '9': (2,3)
  }

prohibited1 = (0,0)

coords2 = {
  '<': (0,0),
  'v': (1,0),
  '>': (2,0),
  '^': (1,1),
  'A': (2,1)
  }


prohibited2 = (0,1)

rev1 = {v:k for k,v in coords1.items()}
rev2 = {v:k for k,v in coords2.items()}

from functools import cache


keys = '<v>^A'
transitions = [(i,j) for i in keys for j in keys]


def to_dct(x):
  dct = {}
  for t in transitions:
    dct[t] = sum(1 for i in x if i == t)
  return dct

def add_dct(d1,d2):
  return {k: d1[k] + d2[k] for k in transitions}

# We are working with transitions
# Symbols are < v > ^ A
# Note down all transitions
transition_matrix = {
('<','<'): [('A','A')],
('<','v'): [('A','>'),('>','A')],
('<','>'): [('A','>'),('>','>'),('>','A')],
('<','^'): [('A','>'),('>','^'),('^','A')],
('<','A'): [('A','>'),('>','>'),('>','^'),('^','A')],

('v','<'): [('A','<'),('<','A')],
('v','v'): [('A','A')],
('v','>'): [('A','>'),('>','A')],
('v','^'): [('A','^'),('^','A')],
# Transition ('v','A') is replaced by [('A','>'),('>','^'),('^','A')] or
# Transition ('v','A') is replaced by [('A','^'),('^','>'),('>','A')]
('v','A'): [('A','^'),('^','>'),('>','A')],

('>','<'): [('A','<'),('<','<'),('<','A')],
('>','v'): [('A','<'),('<','A')],
('>','>'): [('A','A')],
# Transition ('>','^') is replaced by [('A','^'),('^','<'),('<','A')] = 2 + 3 + 4 = 9
# Transition ('>','^') is replaced by [('A','<'),('<','^'),('^','A')] = 4 + 3 + 2 = 9
('>','^'): [('A','<'),('<','^'),('^','A')],
('>','A'): [('A','^'),('^','A')],

('^','<'): [('A','v'),('v','<'),('<','A')],
('^','v'): [('A','v'),('v','A')],
# Transition ('^','>') is replaced by [('A','>'),('>','v'),('v','A')] = 2 + 2 + 3 = 7
# Transition ('^','>') is replaced by [('A','v'),('v','>'),('>','A')] = 2 + 2 + 2 = 6
('^','>'): [('A','v'),('v','>'),('>','A')],
('^','^'): [('A','A')],
('^','A'): [('A','>'),('>','A')],

('A','<'): [('A','v'),('v','<'),('<','<'),('<','A')],
# Transition ('A','v') is replaced by [('A','<'),('<','v'),('v','A')] = 4 + 2 + 3 = 9
# Transition ('A','v') is replaced by [('A','v'),('v','<'),('<','A')] = 3 + 2 + 4 = 9
('A','v'): [('A','v'),('v','<'),('<','A')],
('A','>'): [('A','v'),('v','A')],
('A','^'): [('A','<'),('<','A')],
('A','A'): [('A','A')]
}

import numpy as np

transition_matrix = 
  

def mul(vec):
  dct_new = {k:0 for k in transitions}
  for 

# def sq(x, y, cmd_in):
#   sq_out = [(x,y)]
#   for i in cmd_in:
#     if i == '>':
#       x += 1
#     elif i == '<':
#       x -= 1
#     elif i == '^':
#       y += 1
#     elif i == 'v':
#       y -= 1
#     sq_out += [(x,y)]    
#   return sq_out

# def solve(cmd_in, typ):
#   if typ == 1:
#     x,y = coords1['A']
#   else:
#     x,y = coords2['A']
#   cmd_out = ''
#   for i in cmd_in:
#     if i == 'A':
#       if typ == 1:
#         cmd_out += rev1[(x,y)]
#       else:
#         cmd_out += rev2[(x,y)]
#     elif i == '>':
#       x += 1
#     elif i == '<':
#       x -= 1
#     elif i == '^':
#       y += 1
#     elif i == 'v':
#       y -= 1
#   return cmd_out


# @cache
# def f(p1, p2, typ, nested = False):
#   if typ == 1:
#     x1, y1 = coords1[p1]
#     x2, y2 = coords1[p2]
#   else:
#     x1, y1 = coords2[p1]
#     x2, y2 = coords2[p2]
#   cmd = ''
#   if x2 > x1:
#     cmd += '>'*(x2-x1)
#   if x2 < x1:
#     cmd += '<'*(x1-x2)
#   if y2 < y1:
#     cmd += 'v'*(y1-y2)
#   if y2 > y1:
#     cmd += '^'*(y2-y1)    
#   cmds = []
#   if typ == 1:
#     sq_out = sq(x1, y1, cmd)
#     if prohibited1 not in sq_out:
#       cmds.append(cmd+'A')
#     sq_out = sq(x1, y1, cmd[::-1])
#     if prohibited1 not in sq_out:
#       cmds.append(cmd[::-1]+'A')
#   elif typ == 2:
#     sq_out = sq(x1, y1, cmd)
#     if prohibited2 not in sq_out:
#       cmds.append(cmd+'A')
#     sq_out = sq(x1, y1, cmd[::-1])
#     if prohibited2 not in sq_out:
#       cmds.append(cmd[::-1]+'A')
  
#   cmds = list(set(cmds))
  
#   # Now you should find out in THIS function directly, which of these two commands performs better in the next level up
#   if nested:
#     if len(cmds) > 1:
#       res1 = translate(cmds[0], 2)
#       res2 = translate(cmds[1], 2)
#       minl1 = min(len(i) for i in res1)
#       minl2 = min(len(i) for i in res2)
#       if minl1 < minl2:
#         return [cmd[0]]
  
#   return cmds

# @cache
# def translate(cmd_in, typ):
#   cmd_out = ['']
#   for j in range(len(cmd_in)):
#     if j == 0:
#       x1 = 'A'
#     else:
#       x1 = cmd_in[j-1]
#     x2 = cmd_in[j]
#     cmd = f(x1,x2,typ)
#     cmd_out = [c1+c2 for c1 in cmd_out for c2 in cmd]
#   return cmd_out

# def tt(cmds_in, typ):
#   cmd_out = []
#   for cmd_in in cmds_in:
#     cmd_out += translate(cmd_in, typ)
#   return cmd_out

# s = 0
# d = open('21_test').read().splitlines()
# for cmd_in in d:
#   tmp = tt([cmd_in], 1)
#   for i in range(3):
#     tmp = tt(tmp,2)
#     min_l = min(len(i) for i in tmp)
#     tmp = [i for i in tmp if len(i) == min_l] 
#   fac1 = min(len(i) for i in tmp)
#   fac2 = int(cmd_in[:-1])
#   s += fac1 * fac2
#   print("cmd_in",cmd_in,"fac1",fac1,"fac2",fac2)
# print(s)