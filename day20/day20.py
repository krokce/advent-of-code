import numpy as np

with open('day20.txt', 'r') as file:
  enhancement_algo, image = file.read().strip().split("\n\n")

image = image.replace("#", "1").replace(".", "0")
enhancement_algo = enhancement_algo.replace("#", "1").replace(".", "0")

arr = []
for l in image.split("\n"):
  arr.append([int(i.strip()) for i in l])

arr = np.array(arr)

for i in range(50):
  arr = np.pad(arr, (2,2), constant_values=i%2) # constant_values=0
  size = arr.shape
  new_arr = np.zeros(size).astype(int)

  for row in range(1, size[0]-1):
    for col in range(1, size[1]-1):
      filter = np.ravel( arr[row-1:row+2, col-1:col+2] )
      num = int("".join([str(i) for i in list(filter)]), 2)
      new_arr[row,col] = enhancement_algo[num]
  
  arr = np.array(new_arr[1:-1,1:-1])
  if i == 1:
    print(np.sum(arr))

print(np.sum(arr))