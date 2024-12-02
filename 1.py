d = open('/home/chicotobi/Downloads/1').readlines()
d = [[int(j) for j in i.split()] for i in d]

l1 = sorted(i[0] for i in d)
l2 = sorted(i[1] for i in d)

print(sum(abs(i-j) for i,j in zip(l1,l2)))

s = 0
for i in l1:
  k = sum(1 for j in l2 if j == i)
  s += i * k
print(s)