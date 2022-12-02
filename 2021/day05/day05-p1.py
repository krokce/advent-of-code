file = open('day05.txt', 'r').readlines()

D = {}
lines = []
for l in file:
  x1, y1, x2, y2 = [int(x) for row in [i.split(",") for i in l.strip().split(" -> ")] for x in row]

  if x1 == x2:
    for y in range(min(y1,y2), max(y1,y2)+1):
      if (x1, y) in D:
        D[(x1, y)] += 1
      else:
        D[(x1, y)] = 1

  if y1 == y2:
    for x in range(min(x1,x2), max(x1,x2)+1):
      if (x, y1) in D:
        D[(x, y1)] += 1
      else:
        D[(x, y1)] = 1

print(sum(1 for i in D.values() if i > 1))