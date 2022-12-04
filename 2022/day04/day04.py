import re
with open('day04.txt', 'r') as file:
  input = [l.strip() for l in file.readlines()]

contain = 0
overlap = 0
for l in input:
  r = [int(i) for i in re.findall(r"\d+", l)]
  e1 = set(range(r[0],r[1]+1))
  e2 = set(range(r[2],r[3]+1))
  if len(e1 & e2) == min(len(e1), len(e2)):
    contain += 1
  if len(e1 & e2) > 0:
    overlap += 1

#1
print(contain)

#2
print(overlap)