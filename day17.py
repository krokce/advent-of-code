with open('day17.txt', 'r') as file:
  l = file.read().strip()

import re
target_min_x, target_max_x, target_min_y, target_max_y = [int(p) for p in re.findall(r"-?\d+", l)]

def step(P, n, v0x, v0y):
  vx = v0x - n + 1 if n < v0x else 0
  vy = v0y - n + 1
  if n in P:
    return P[n]
  elif n == 1:
    P[n] = (vx,vy)
    return P[n]
  else:
    x = P[n-1][0] + vx
    y = P[n-1][1] + vy
    P[n] = (x,y)
    return P[n]

def shot(P, v0x, v0y):
  ymax = 0
  n = 0
  while True:
    p = step(P, n, v0x, v0y)
    ymax = max(ymax, p[1])
    if p[0] > target_max_x or p[1] < target_min_y:
      return False, 0
    elif target_min_x <= p[0] <= target_max_x and  target_min_y <= p[1] <= target_max_y:
      return True, ymax 
    n += 1

ret = 0
V = []

for v0x in range(target_max_x+1):
  for v0y in range(target_min_y-1, abs(target_min_y)+1):
    P = {0: (0,0)}
    success, ymax = shot(P, v0x, v0y)
    if success:
      ret = max(ret, ymax)
      V.append((v0x, v0y))

# 1
print(ret)

# 2
print(len(V))