lines = open('day01.txt', 'r').readlines()

# 1
cur = None
ret = 0
for l in lines:
  n = int(l.strip())
  if cur and n > cur:
    ret = ret + 1
  cur = n

print(ret)

# 2
arr = []
for l in lines:
  l = int(l.strip())
  arr.append(l)

cur = None
ret = 0
for i in range(1, len(arr)-1):
  s = sum(arr[i-1:i+2])
  if cur and s > cur:
    ret = ret + 1
  cur = s

print(ret)