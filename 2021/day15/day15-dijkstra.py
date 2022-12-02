with open('day15.txt', 'r') as file:
  input = [l.strip() for l in file.readlines()]

map = []
directions = [(0,-1),(-1,0),(1,0),(0,1)]

for l in input:
  map.append([int(i) for i in l])

size_rows = len(map)
size_cols = len(map[0])

R={}

for row in range(size_rows):
  for col in range(size_cols):
    for i in range(5):
      for j in range(5):
        r = (map[row][col] + i + j) if (map[row][col] + i + j) < 10 else ((map[row][col] + i + j) % 10 + 1)
        R[(row + i*size_rows, col+j*size_cols)] = r

size_cols = 0
size_rows = 0
for k in R.keys():
  size_rows = max(k[0], size_rows)
  size_cols = max(k[1], size_cols)

# for row in range(size_rows):
#   for col in range(size_cols):
#     r = (map[row][col]) 
#     R[(row, col)] = r

import heapq

Q = []
heapq.heappush(Q, (0,0,0))

V = set()
D = {}
while True:
  r, row, col = heapq.heappop(Q)
  if (row, col) in V:
    continue
  if (row, col) == (size_rows, size_cols):
    print(r)
    break
  for d in directions:
    p = (row + d[0], col + d[1])
    if p in V:
      continue
    if p not in R:
      continue
    if p in D and D[p] < R[p] + r:
      continue
    D[p] = R[p] + r
    heapq.heappush(Q, (R[p] + r, *p))
    V.add((row, col))