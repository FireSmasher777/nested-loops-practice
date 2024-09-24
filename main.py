a = 20
b = 30
count = 0
if a < 0:
  a = -a
if b < 0:
  b = -b 

while b > 0:
  while b <= a:
    a = a - b
  c = a
  a = b
  b = c
  
  count += 1
  print("Loop # ", count) 
  print("a is", a)
  print("b is", b)
  print("c is", c)


print()
print("Final count of a is", a)



print()

num = int(input())
if num > 0:
  print(-num, "The number is negative")
else:
  print(num * -1, "The number is positive")

