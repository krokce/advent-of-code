with open('day10.txt', 'r') as file:
  input = [l.strip().split(" ") for l in file.readlines()]

X = 1
clock = [1]
for instruction in input:
  if instruction[0] == "noop":
    clock += [X]
  if instruction[0] == "addx":
    clock += [X, X]
    X += int(instruction[1])

#1
print(sum([c*clock[c] for c in range(20, len(clock), 40)]))

crt = []
for cycle in range(1, len(clock)):
  pixel = cycle-1
  sprite = clock[cycle]
  if clock[cycle]-1 <= pixel%40 <= clock[cycle]+1:
    crt.append('#')
  else:
    crt.append('.')

#2
for x in range(0, len(crt), 40):
  print("".join(crt[x:x+40]))