from copy import deepcopy as dc

floor = []
with open('day25.txt', 'r') as file:
  floor = [[c for c in k] for k in [l.strip() for l in file.readlines()]]

def do_move(floor, new_floor, t, row, col):
  if t == ">":
    if col == len(floor[row])-1:
      target = (row, 0)
    else:
      target = (row, col+1)

    if floor[target[0]][target[1]] == ".":
      new_floor[target[0]][target[1]] = ">"
      new_floor[row][col] = "."
      return True
    else:
      new_floor[row][col] = ">"
      return False

  elif t == "v":
    if row == len(floor)-1:
      target = (0, col)
    else:
      target = (row+1, col)

    if floor[target[0]][target[1]] == ".":
      new_floor[target[0]][target[1]] = "v"
      new_floor[row][col] = "."
      return True
    else:
      new_floor[row][col] = "v"
      return False
  return False

def step(t, floor, new_floor):
  changes = 0
  for row in range(len(floor)):
    for col in range(len(floor[row])):
      if floor[row][col] == t:
        if do_move(floor, new_floor, t, row, col):
          changes += 1
      if t == ">" and floor[row][col] not in (">", "."):
        new_floor[row][col] = floor[row][col]
  return changes

ret = 0
while True:
  new_floor = [["." for col in range(len(floor[0]))] for row in range(len(floor))]
  c1 = step(">", floor, new_floor)
  new_floor_v = dc(new_floor)
  c2 = step("v", new_floor, new_floor_v)
  floor = new_floor_v
  ret += 1
  if c1+c2 == 0:
    break

print(ret)