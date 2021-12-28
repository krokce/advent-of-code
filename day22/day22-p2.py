import re

with open('day22.txt', 'r') as file:
  lines = [l.strip() for l in file.readlines()]


steps = []
actions = []
for l in lines:
  c = [int(c) for c in re.findall(r"-?\d+", l)]
  a = l.split(" ")[0]
  steps.append(c)
  actions.append(a)

def intersection(c1, c2):
  ix1, ix2 = max(c1[0], c2[0]), min(c1[1], c2[1])
  iy1, iy2 = max(c1[2], c2[2]), min(c1[3], c2[3])
  iz1, iz2 = max(c1[4], c2[4]), min(c1[5], c2[5])
  if ix1 <= ix2 and iy1 <= iy2 and iz1 <= iz2:
      return (ix1, ix2, iy1, iy2, iz1, iz2)

def volume(c):
  return (c[1]-c[0]+1) * (c[3]-c[2]+1) * (c[5]-c[4]+1)

volumes = []
done_steps = []
signs = []

# Implements: https://en.wikipedia.org/wiki/Inclusion%E2%80%93exclusion_principle

for i in range(len(steps)):
  new_cuboid = steps[i]
  tmp = done_steps.copy()
  
  for step_id, cuboid in enumerate(done_steps):
    intersect = intersection(new_cuboid, cuboid)
    if intersect:
      tmp.append(intersect)
      volumes.append(-signs[step_id] * volume(intersect))
      signs.append(-signs[step_id])
  
  if actions[i] == "on":
    tmp.append(new_cuboid)
    volumes.append(volume(new_cuboid))
    signs.append(1)

  done_steps = tmp

print(sum(volumes))