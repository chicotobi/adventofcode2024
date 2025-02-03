import numpy as np
import random

# 220493992841852

keys = '<v>^A'
transitions = [i+j for i in keys for j in keys]
transitions = dict(zip(transitions,range(len(transitions))))
 
def expand2(s):
  s = 'A' + s + 'A'
  v = []
  for i in range(len(s)-1):
    v += [s[i:i+2]]
  return v

def expand(s):
  s = 'A' + s
  v = np.zeros((25,1), dtype = 'int64')
  for i in range(len(s)-1):
    el = s[i:i+2]
    idx = transitions[el]
    v[idx] += 1
  return v
   
def create_matrix():
  # Keys are two-element transitions between states
  # Values are presses to be executed
  transition_matrix = {
  '<<': [''],
  '<v': ['>'],
  '<>': ['>>'],
  '<^': ['>^'],
  '<A': ['>>^'],
  
  'v<': ['<'],
  'vv': [''],
  'v>': ['>'],
  'v^': ['^'],
  'vA': ['^>','>^'],
  
  '><': ['<<'],
  '>v': ['<'],
  '>>': [''],
  '>^': ['^<','<^'],
  '>A': ['^'],
  
  '^<': ['v<'],
  '^v': ['v'],
  '^>': ['v>','>v'],
  '^^': [''],
  '^A': ['>'],
  
  'A<': ['v<<'],
  'Av': ['v<','<v'],
  'A>': ['v'],
  'A^': ['<'],
  'AA': ['']
  }
  
  # Expand the form
  for k, v in transition_matrix.items():
    v2 = expand2(random.choice(v))
    transition_matrix[k] = v2
  
  mat = np.zeros((25,25), dtype = 'int64')
  for el1, v in transition_matrix.items():
    for el2 in v:
      i = transitions[el2]
      j = transitions[el1]
      mat[i,j] += 1
  return transition_matrix, mat

def number_encode(s):
  dct = {
    'A0': ['<'],
    '02': ['^'],
    '29': ['^^>','>^^'],
    '9A': ['vvv'],
    'A9': ['^^^'],
    '98': ['<'],
    '80': ['vvv'],
    '0A': ['>'],
    'A1': ['^<<'],
    '17': ['^^'],
    '79': ['>>'],
    'A4': ['^^<<'],
    '45': ['>'],
    '56': ['>'],
    '6A': ['vv'],
    'A3': ['^'],
    '37': ['<<^^','^^<<'],
    '41': ['v'],
    '13': ['>>'],
    '3A': ['v'],
    '48': ['^>','>^'], 
    'A6': ['^^'],
    '68': ['^<','<^'],
    '82': ['vv'],
    '2A': ['v>','>v'],
    'A8': ['<^^^','^^^<'],
    '87': ['<'],
    '08': ['^^^'],
    '83': ['vv>','>vv']
    }
  s = 'A' + s
  code = ['']
  for i in range(len(s)-1):
    sub = s[i:i+2]
    tmp = [i+'A' for i in dct[sub]]
    code = [c1+c2 for c1 in code for c2 in tmp]
  return code

d = open('21').read().splitlines()
DEPTH = 25

# Destroy it with random-ness
best_sum = 1e20
for random_try in range(100):
  raw, mat = create_matrix()
  s = 0
  for cmd_in in d:
    fac2 = int(cmd_in[:-1])
    codes = number_encode(cmd_in)
    min_fac1 = 1e20
    for code in codes:
      v = expand(code)
      for depth in range(DEPTH):
        v = mat.dot(v)
      fac1 = np.sum(v)
      #print("  cmd_in",cmd_in,"fac1",fac1,"fac2",fac2) 
      min_fac1 = min(min_fac1, fac1)
    s += min_fac1 * fac2
    #print("cmd_in",cmd_in,"min_fac1",min_fac1,"fac2",fac2)
  best_sum = min(best_sum, s)
  print("best_sum", best_sum)