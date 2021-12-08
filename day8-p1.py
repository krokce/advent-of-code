with open('day8.txt', 'r') as file:
  input = [l.strip() for l in file.readlines()]

N = {3:7, 7:8, 2:1, 4:4}
ret = 0

for l in input:
  signal, output = l.split(" | ")
  for digit in output.split(" "):
    if len(digit) in N:
      ret += 1

print(ret)