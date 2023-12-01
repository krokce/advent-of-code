import numpy as np
from matplotlib import pyplot as plt

size = (6, 25)
with open('day08.txt', 'r') as file:
  a = np.array([c for c in file.read()])

start = 0
layers = []
for end in range(size[0]*size[1], len(a)+1, size[0]*size[1]):
  arr = np.array(np.reshape(a[start:end], size).astype(int))
  layers.append(arr)
  start = end

min_zeros = 1e9
for l in layers:
  v, c = np.unique(l, return_counts=True)
  lc = dict(zip(v,c))
  if lc[0] < min_zeros:
    min_zeros = lc[0]
    ret = lc[1] * lc[2]

# 1
print(ret)

# 2
for row in range(size[0]):
  for col in range(size[1]):
    for l in layers:
      if l[row,col] == 2:
        continue
      print("#" if l[row,col] == 1 else " ", end='')
      break
  print()
