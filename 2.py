d = [[int(j) for j in i.split()] for i in open('2').readlines()]

def is_save(x):
  diffs = [x[j+1] - x[j] for j in range(len(x)-1)] 
  if all(j<0 for j in diffs) or all(j>0 for j in diffs):
    if max(abs(j) for j in diffs) < 4:
      return True
  return False

s = 0
for i in d:
  
  if is_save(i):
    s += 1
  else:
    for j in range(len(i)):
      i2 = i.copy()
      i2.pop(j)
      if is_save(i2):
        s += 1
        break
  
    