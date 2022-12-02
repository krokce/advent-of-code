import re

with open('day22.txt', 'r') as file:
  lines = [l.strip() for l in file.readlines()]

moves = []
for l in lines:
  c = [int(c) for c in re.findall(r"-?\d+", l)]
  a = l.split(" ")[0]
  moves.append(c+[a])

def lim(c):
  if c < -50:
    return -50
  elif c > 50:
    return 50
  else:
    return c

C = set()
for m in moves:
  if min(m[:6]) < -50 or max(m[:6]) > 50:
    pass
  xmin, xmax, ymin, ymax, zmin, zmax = m[0], m[1], m[2], m[3], m[4], m[5]
  for x in range(m[0], m[1]+1):
    for y in range(m[2], m[3]+1):
      for z in range(m[4], m[5]+1):
        if m[6] == "on":
          C.add((x,y,z))
        else:
          C -= {(x,y,z)}
  print(len(C))