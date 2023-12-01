from collections import defaultdict

with open('day09.txt', 'r') as file:
  l = file.read()

l = {i:int(v) for i, v in enumerate(l.split(","))}

def intcode(n):
  pointer = 0
  relative_base = 0
  instructions = defaultdict(int, l.copy())

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
      instructions[address[1]] = n
      pointer += 2

    elif opcode == 4:
      print("Output value: {}".format(instructions[address[1]]))
      pointer += 2

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

  return 0

# 1
intcode(1)

# 2
intcode(2)