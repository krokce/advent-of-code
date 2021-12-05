file = open('day5.txt', 'r').readlines()

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

  elif y1 == y2:
    for x in range(min(x1,x2), max(x1,x2)+1):
      if (x, y1) in D:
        D[(x, y1)] += 1
      else:
        D[(x, y1)] = 1

  elif abs(x2 - x1) == abs(y2 - y1):
    xinc = (x2-x1) / abs(x2-x1)
    yinc = (y2-y1) / abs(y2-y1)

    x = x1
    y = y1

    for i in range(abs(x2-x1)+1):
      if (x, y) in D:
        D[(x, y)] += 1
      else:
        D[(x, y)] = 1
      
      x += xinc
      y += yinc

ret = 0
for v in D.values():
  if v > 1:
    ret += 1

print(ret)