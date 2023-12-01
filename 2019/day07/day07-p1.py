from itertools import permutations

with open('day07.txt', 'r') as file:
  l = file.read()

l = [int(i) for i in l.split(",")]

def intcode(inputs):
  pointer = 0
  instructions = l.copy()

  while 0 <= pointer < len(instructions)-2:
    opcode = str(instructions[pointer])
    opcode = opcode.rjust(5, "0")
    param2 = int(opcode[1])
    param1 = int(opcode[2])
    opcode = int(opcode[3:5])

    address1 = instructions[pointer + 1] if param1 == 0 else pointer + 1    
    address2 = instructions[pointer + 2] if param2 == 0 else pointer + 2

    if opcode == 99:
      break

    elif opcode == 1:
      instructions[instructions[pointer + 3]] = instructions[address1] + instructions[address2]
      pointer += 4

    elif opcode == 2:
      instructions[instructions[pointer + 3]] = instructions[address1] * instructions[address2]
      pointer += 4

    elif opcode == 3:
      instructions[address1] = inputs.pop(0)
      pointer += 2

    elif opcode == 4:
      if instructions[address1] != 0:
        return instructions[address1]
      pointer += 2

    elif opcode == 5:
      if instructions[address1] != 0:
        pointer = instructions[address2]
      else:
        pointer += 3

    elif opcode == 6:
      if instructions[address1] == 0:
        pointer = instructions[address2]
      else:
        pointer += 3

    elif opcode == 7:
      if instructions[address1] < instructions[address2]:
        instructions[instructions[pointer + 3]] = 1
      else: 
        instructions[instructions[pointer + 3]] = 0
      pointer += 4

    elif opcode == 8: 
      if instructions[address1] == instructions[address2]:
        instructions[instructions[pointer + 3]] = 1
      else:
        instructions[instructions[pointer + 3]] = 0
      pointer += 4

  return 0

def sequence(s):
  output = 0
  for n in s:
    output = intcode([n, output])
  return output

ret = 0
for s in permutations(list(range(5))):
    ret = max(ret, sequence(list(s)))

print(ret)