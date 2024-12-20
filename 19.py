from functools import cache

d = open('19').read().splitlines()

given = d[0].split(', ')
todo = d[2:]

@cache
def is_possible(s):
  if s == '':
    return 1
  v = 0
  for g in given:
    if s[:len(g)] == g:
      v += is_possible(s[len(g):])
  return v

s = sum(is_possible(s) for s in todo)
print(s)
  