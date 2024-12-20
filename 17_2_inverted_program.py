v = [1, 5, 0, 5, 2, 0, 1, 3, 5]

a = 0
b = 5
c = 1

for i in v:
  b = b ^ c ^ 5
  print("a",a,"b",b,"c",c)
  a = 8 * a + (b ^ 3)
  print("a",a,"b",b,"c",c)
  c = a // 2 ** b
  print("a",a,"b",b,"c",c)

print(a)