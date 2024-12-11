from functools import cache

@cache
def rule(el, n):
  if el == '0':
    res = ['1',]
  elif len(el) % 2 == 0:            
    length = len(el)
    res = [el[:length//2], str(int(el[length//2:]))]
  else:
    res = [str(2024*int(el))]
  if n == 1:
    return len(res)
  else:
    return count_stones(res, n - 1)

def count_stones(lst, n):
  return sum(rule(el, n) for el in lst)

d = open('11').read().splitlines()[0].split()
print(count_stones(d,25))
print(count_stones(d,75))