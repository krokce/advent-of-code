from collections import defaultdict
from copy import deepcopy

with open('day13.txt', 'r') as file:
  l = file.read()

l = {i:int(v) for i, v in enumerate(l.split(","))}

relative_base = 0
instructions = defaultdict(int, l)
pointer = 0

def intcode(input_instruction):
  global relative_base
  global pointer

  while True and 0 <= pointer < len(instructions)-2:
    instruction_code = str(instructions[pointer])
    instruction_code = instruction_code.rjust(5, "0")

    # Parameter mode: 
    # (0) position mode, (1) immediate mode, (2) relative mode
    address = defaultdict(int, {})
    for id, mode in enumerate([int(i) for i in instruction_code[0:3]]):
      id = 3-id
      if mode == 0:
        address[id] = instructions[pointer + id]

      elif mode == 1: 
        address[id] = pointer + id

      elif mode == 2: 
        address[id] = instructions[pointer + id] + relative_base
    
    # Operation code
    opcode = int(instruction_code[3:5])
      
    if opcode == 99:
      break

    elif opcode == 1:
      instructions[address[3]] = instructions[address[1]] + instructions[address[2]]
      pointer += 4

    elif opcode == 2:
      instructions[address[3]] = instructions[address[1]] * instructions[address[2]]
      pointer += 4

    elif opcode == 3:
      instructions[address[1]] = input_instruction
      pointer += 2

    elif opcode == 4:
      pointer += 2
      return instructions[address[1]]

    elif opcode == 5:
      if instructions[address[1]] != 0:
        pointer = instructions[address[2]]
      else:
        pointer += 3

    elif opcode == 6:
      if instructions[address[1]] == 0:
        pointer = instructions[address[2]]
      else:
        pointer += 3

    elif opcode == 7:
      if instructions[address[1]] < instructions[address[2]]:
        instructions[address[3]] = 1
      else: 
        instructions[address[3]] = 0
      pointer += 4

    elif opcode == 8: 
      if instructions[address[1]] == instructions[address[2]]:
        instructions[address[3]] = 1
      else:
        instructions[address[3]] = 0
      pointer += 4

    elif opcode == 9: 
      if instructions[address[1]] != 0:
        relative_base += instructions[address[1]]
      pointer += 2
  return None

cnt = 0
ret = 0
while True:
    v = intcode(None)
    cnt += 1
    if cnt % 3 == 0:
        if v == 2:
            ret += 1
    if v is None:
        break

print(ret)
print(cnt)