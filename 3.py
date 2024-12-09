import re

d = open('3').read()
out = [[int(j) for j in i[4:-1].split(',')] for i in re.findall('mul\([0-9]+,[0-9]+\)',d)]
out2 = sum(i[0]*i[1] for i in out)
print(out2)

out = re.findall('mul\([0-9]+,[0-9]+\)|do\(\)|don\'t\(\)',d)

s = 0
enabled = True
for word in out:
  if word == 'do()':
    enabled = True
    continue
  if word == 'don\'t()':
    enabled = False
    continue
  if enabled:
    #print(word)
    nums = [int(j) for j in word[4:-1].split(',')]
    prod = nums[0] * nums[1]
    s += prod
print(s)