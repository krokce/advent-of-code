with open('day11.txt', 'r') as file:
  input = [l.strip() for l in file.readlines()]

P = {(x,y):int(v) for y in range(len(input)) for x,v in enumerate(input[y])}
directions = [-1, 0 , 1]

def rest():
  for k, v in P.items():
    P[k] += 1

def flash(F):
  for k, v in P.items():
    if v == 10 and k not in F:
      F.add(k)
      for drow in directions:
        for dcol in directions:
          row, col = (k[0] + drow), (k[1] + dcol)
          if (row, col) in P and P[(row, col)] < 10:
            P[(row, col)] += 1
      return True

def release(F):
  for e in F:
    P[e] = 0

days = 0
flashes = 0

while True:
  F = set()
  rest()
  while flash(F):
    flashes += 1
  release(F)
  days += 1
  if days == 100:
    print(flashes)
  if len(F) == len(P):
    print(days)
    break