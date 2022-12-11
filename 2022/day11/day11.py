import math
from copy import deepcopy

with open('day11.txt', 'r') as file:
  input = [l.strip().split(":") for l in file.readlines()]

monkey = {}
current_monkey = 0
for i in input:
  if "Monkey" in i[0]:
    monkey[int(i[0][-1])] = {"item_count": 0}
    current_monkey = int(i[0][-1])
  elif "Starting items" in i[0]:
    monkey[current_monkey]["items"] = ([int(item) for item in reversed(i[1].strip().split(","))])
  elif "Operation" in i[0]:
    monkey[current_monkey]["operation"] = i[1].strip().split("=")[1]
  elif "Test" in i[0]:
    monkey[current_monkey]["test"] = int(i[1].split(" ")[-1])
  elif "If true" in i[0]:
    monkey[current_monkey]["true"] = int(i[1].split(" ")[-1])
  elif "If false" in i[0]:
    monkey[current_monkey]["false"] = int(i[1].split(" ")[-1])


def solve(M, rounds, part_one):
  p = math.prod([m["test"] for m in M.values()])

  for r in range(rounds):
    for monkey_id, monkey in M.items():
      for _ in range(len(monkey["items"])):
        M[monkey_id]["item_count"] += 1
        old = M[monkey_id]["items"].pop()
        old = eval(M[monkey_id]["operation"]) // (3 if part_one else 1)

        if old % M[monkey_id]["test"] == 0:
          M[M[monkey_id]["true"]]["items"].append(old%p) 
        else:
          M[M[monkey_id]["false"]]["items"].append(old%p) 

  return math.prod(sorted([m["item_count"] for m in M.values()])[-2:])

#1
print(solve(deepcopy(monkey), 20, True))

#2
print(solve(deepcopy(monkey), 10000, False))