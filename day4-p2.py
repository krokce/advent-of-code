lines = open('day4.txt', 'r').readlines()
lines = [l.strip() for l in lines]

l = []
T = {}
tidx = 0

for idx in range(len(lines)):
  if idx == 0:
    l = list(map(int, lines[idx].split(",")))
  else:
    if len(lines[idx]) < 1:
      tidx += 1
      continue
    else:
      if tidx not in T:
        T[tidx] = []
      T[tidx].append( [int(i) for i in lines[idx].split(" ") if i != ""] )

def new_number(n):
  for k, v in T.items():
    for x in range(len(v)):
      if n in v[x]:
        col = v[x].index(n)
        T[k][x][col] = -1
        if sum([i for i in T[k][x] if i != -1]) == 0 or sum([i for row in T[k] for i in [row[col]] if i != -1]) == 0: 
          if k not in winners:
            winners.append(k)
          if len(winners) == len(T):
            return (True, T[k])
  return (False, [])

winners = []
for n in l:
  is_bingo, board = new_number(n)
  if is_bingo:
    print(sum([i for row in board for i in row if i != -1]) * n)
    break