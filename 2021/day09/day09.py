with open('day09.txt', 'r') as file:
  input = [l.strip() for l in file.readlines()]

map = []
for l in input:
  map.append([int(i) for i in l])

# 1
P = {}
directions = [(-1,0), (1,0), (0,-1), (0,1)]

for row in range(len(map)):
  for col in range(len(map[row])):
    low = 0
    for drow, dcol in directions:
      if row+drow < 0 or row+drow >= len(map) or col+dcol < 0 or col+dcol >= len(map[row]):
        low += 1
      else:
        if map[row+drow][col+dcol] > map[row][col]:
          low += 1
    if low == 4:
      P[(row,col)] = map[row][col]

print(sum(1+i for i in P.values()))

# 2
bsize = []

def basin_size(row, col, B):
  for drow, dcol in directions:
    if not (row+drow < 0 or row+drow >= len(map) or col+dcol < 0 or col+dcol >= len(map[row])):
      if map[row+drow][col+dcol] < 9:
        B.add((row, col))
        if (row+drow, col+dcol) not in B:
          basin_size(row+drow, col+dcol, B)

for k, v in P.items():
  B = set()
  basin_size(k[0], k[1], B)
  bsize.append(len(B))

bsize.sort()
bsize.reverse()
print(bsize[0] * bsize[1] * bsize[2])