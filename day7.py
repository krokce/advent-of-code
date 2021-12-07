import numpy as np

input = open('day7.txt', 'r').read()
input = list(map(int, input.split(",")))

def fuel(d):
  return sum(i for i in range(d+1))

med = int(np.median(input))
avg = int(np.average(input))

# 1
print(sum(abs(i-med) for i in input))

# 2
print(sum(fuel(abs(i-avg)) for i in input))