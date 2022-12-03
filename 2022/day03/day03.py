with open('day03.txt', 'r') as file:
  input = [l.strip() for l in file.readlines()]

def get_priority(common):
  return ord(common)-38 if common.isupper() else ord(common)-96  

priority1 = 0
for r in input:
  cut = int(len(r)/2)
  (common,) = set(r[0:cut]) & set(r[cut:])
  priority1 += get_priority(common)

priority2 = 0
for i in range(0, len(input), 3):
  (common,) = set(input[i]) & set(input[i+1]) & set(input[i+2])
  priority2 += get_priority(common)

#1
print(priority1)

#2
print(priority2)