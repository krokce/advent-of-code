import math
import itertools

with open('day10.txt', 'r') as file:
  a = [list(c) for c in [r.strip() for r in file.readlines()]]

M = {}
for row in range(len(a)):
  for col in range(len(a[row])):
    if a[row][col] == "#":
      M[col,row] = set()

def scan(p):
  ds = []
  for sx, sy in itertools.product((-1,0,1),(-1,0,1)):
    for dx in range(1,len(a[0])):
      for dy in range(1,len(a)):
        if (sx,sy) in ds or (sx,sy)==(0,0):
          break
        if (sx, sy, dx/dy) in ds:
          continue
        x = p[0] + dx * sx
        y = p[1] + dy * sy
        if (x,y) in M:
            M[p].add((x,y))
            ds.append((sx, sy, dx/dy))
            if 0 in [sx,sy]:
              ds.append((sx,sy))
        elif 0 <= x < len(a[0]) and 0 <= y < len(a):
          continue
        else:
          break
  return len(M[p])

# 1
visible = 0
station = None

for p in M:
  v = scan(p)
  if visible < v:
    visible = v
    station = p

print(visible)

# 2
T = {}
quadrant = {(1,-1): 0, (1,1): math.pi/2, (-1,1): math.pi , (-1,-1): 3*math.pi/2}

for p in M:
  if p != station:
    x = p[0] - station[0]
    y = p[1] - station[1]

    if x == 0:
      distance = abs(y)
      angle = 0 if y < 0 else math.pi
    elif y == 0:
      distance = abs(x)
      angle = 3*math.pi/2 if x < 0 else math.pi/2
    else:
      distance = math.sqrt(x**2+y**2)
      if x > 0:
        angle = math.atan(abs(x)/abs(y)) + quadrant[(x/abs(x), y/abs(y))]
      else:
        angle = math.atan(abs(y)/abs(x)) + quadrant[(x/abs(x), y/abs(y))]

    if angle in T:
      T[angle] = sorted(T[angle] + [(distance, p)])
    else:
      T[angle] = [(distance, p)]

asteroids = [station]
while True:
  chg = 0
  for k in sorted(T):
    if len(T[k]) > 0:
      asteroids.append(T[k].pop(0)[1])
      chg += 1
  if chg == 0:
    break

print(asteroids[200][0]*100 + asteroids[200][1])