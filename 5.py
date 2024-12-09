d = open('5').read().splitlines()


def check(update):
  correct = True
  n = len(update)
  for i in range(n):
    for j in range(i+1,n):
      for x, y in rules:
        if update[i] == y and update[j] == x:
          correct = False
          
  if correct:
    return update[n//2], 0
  else:
    # Fix
    for i in range(n):
      for j in range(i+1,n):
        for x, y in rules:
          if update[i] == y and update[j] == x:
            update[i] = x
            update[j] = y
    return 0, update[n//2]

rules = []
into = 'rules'
s1 = 0
s2 = 0
for i in d:
  if i == '':
    into = 'updates'
    continue
  if into == 'rules':
    x, y = i.split('|')
    x = int(x)
    y = int(y)
    rules.append([x,y])    
  else:
    update = [int(j) for j in i.split(',')]
    a1, a2 = check(update)
    s1 += a1
    s2 += a2

print(s1,s2)