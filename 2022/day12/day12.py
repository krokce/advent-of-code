import heapq

with open('day12.txt', 'r') as file:
  input = [l.strip() for l in file.readlines()]

size_rows = len(input)
size_cols = len(input[0])

H = {}
possible_starts = []

for row in range(size_rows):
  for col in range(size_cols):
    if input[row][col] == "S":
      H[(row,col)] = 0
      start = [(row,col)]
    elif input[row][col] == "E":
      H[(row,col)] = ord("z") - ord("a")
      end = (row,col)
    else:
      H[(row,col)] = ord(input[row][col])-ord("a")
    #2
    if input[row][col] == "a":
      possible_starts.append((row,col))

def solve(start):
  Q = []

  for s in start:
    heapq.heappush(Q, (0, *s))

  visited = set()
  scores = {}
 
  while True:
    score, row, col = heapq.heappop(Q)
    if (row, col) in visited:
      continue
    if (row, col) == end:
      return score
    for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
      p = (row + d[0], col + d[1])
      if p in visited:
        continue
      if p not in H or H[p] - H[(row, col)] > 1:
        continue
      if p in scores and scores[p] < score + 1:
        continue
      scores[p] = score + 1
      heapq.heappush(Q, (score + 1, *p))
      visited.add((row, col))

#1
print(solve(start))

#2
print(solve(possible_starts))