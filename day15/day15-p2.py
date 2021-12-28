with open('day15.txt', 'r') as file:
  input = [l.strip() for l in file.readlines()]

map = []
directions = [(0,-1),(-1,0),(1,0),(0,1)]

for l in input:
  map.append([int(i) for i in l])

size_rows = len(map)
size_cols = len(map[0])

D={}

for row in range(size_rows):
  for col in range(size_cols):
    for i in range(5):
      for j in range(5):
        r = (map[row][col] + i + j) if (map[row][col] + i + j) < 10 else ((map[row][col] + i + j) % 10 + 1)
        D[(row + i*size_rows, col+j*size_cols)] = r

size_cols = 0
size_rows = 0
for k in D.keys():
  size_rows = max(k[0], size_rows)
  size_cols = max(k[1], size_cols)

R={}

def update(p):
  risks = []
  for d in directions:
    pn = (p[0] + d[0], p[1] + d[1])
    if pn in R:
      risks.append(R[pn] + D[p])
  if p not in R or R[p] > min(risks):
    R[p] = min(risks)
    return True
  return False

cur = (size_rows, size_cols)
R[cur] = D[cur]

tmp = [k for k in R.keys()]

while True:
  changes = 0  
  chg_list = []
  
  for k in tmp:
    for d in directions:
      pn = (k[0] + d[0], k[1] + d[1])
      if pn in D:
        if update(pn):
          changes += 1
          chg_list.append(pn)
  tmp = chg_list
  if changes == 0:
    break

print(R[(0,0)] - D[(0,0)])