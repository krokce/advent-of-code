import math

with open('day08.txt', 'r') as file:
  input = [l.strip() for l in file.readlines()]

tree = {}
seen = set()

x_max = len(input)
y_max = len(input[0])

for y in range(y_max):
  for x in range(x_max):
    tree[(x,y)] = int(input[y][x])

for x in range(x_max):
  min_tree = -1
  for y in range(y_max):
    if tree[(x,y)] > min_tree:
      seen.add((x,y))
      min_tree = tree[(x,y)]

  min_tree = -1
  for y in range(y_max-1, -1, -1):
    if tree[(x,y)] > min_tree:
      seen.add((x,y))
      min_tree = tree[(x,y)]

for y in range(y_max):
  min_tree = -1
  for x in range(x_max):
    if tree[(x,y)] > min_tree:
      seen.add((x,y))
      min_tree = tree[(x,y)]

  min_tree = -1
  for x in range(x_max-1, -1, -1):
    if tree[(x,y)] > min_tree:
      seen.add((x,y))
      min_tree = tree[(x,y)]

def scenic_score(t):
  directions = [1, 0, -1]
  scenic = {}
  for dx in directions:
    for dy in directions:

      if abs(dx) == abs(dy):
        continue

      scenic[(dx, dy)] = 0
      x, y = t[0] + dx, t[1] + dy     
      
      while (x,y) in tree:
        scenic[(dx, dy)] += 1
        if tree[t] <= tree[(x,y)]:
          break
        x, y = x + dx, y + dy

  return(math.prod(scenic.values()))

#1
print(len(seen))

#2
print(max(scenic_score((x,y)) for x in range(x_max) for y in range(y_max)))