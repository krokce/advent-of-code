from matplotlib import pyplot as plt
import numpy as np

with open('day13.txt', 'r') as file:
  input = [l.strip() for l in file.readlines()]

P = {}
folds = []
point_count = []
for l in input:
  if l != "" and "fold" not in l:
    x, y =  map(int, l.split(","))
    P[(x, y)] = 1
  elif "fold" in l:
    str = l.split(" ")[2].split("=")
    folds.append([str[0], int(str[1])])

for axis, n in folds:
  F = {}
  for p in P.keys():
    if axis == "x": 
      if p[0] > n:
        newx = n - (p[0] - n)
        F[(newx, p[1])] = 1
      elif p[0] != n:
        F[(p[0], p[1])] = 1
    if axis == "y":
      if p[1] > n:
        newy = n - (p[1] - n)
        F[(p[0], newy)] = 1
      elif p[1] != n:
        F[(p[0], p[1])] = 1
  P = F
  point_count.append(len(P))

xmax = max([x for x,_ in P.keys()])
ymax = max([y for _,y in P.keys()])

arr = np.zeros((xmax+1, ymax+1))
for p in P.keys():
  arr[p[0], p[1]] = 1

#1
print(point_count[0])

#2
plt.imshow(np.transpose(arr))
plt.show()