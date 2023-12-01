from itertools import permutations

with open('day07.txt', 'r') as file:
  l = file.read()

l = [int(i) for i in l.split(",")]

def intcode(inputs, program, pointer):

  while True and 0 <= pointer < len(program)-2:
    opcode = str(program[pointer])
    opcode = opcode.rjust(5, "0")
    param2 = int(opcode[1])
    param1 = int(opcode[2])
    opcode = int(opcode[3:5])

    address1 = program[pointer + 1] if param1 == 0 else pointer + 1    
    address2 = program[pointer + 2] if param2 == 0 else pointer + 2

    if opcode == 99:
      break

    elif opcode == 1:
      program[program[pointer + 3]] = program[address1] + program[address2]
      pointer += 4

    elif opcode == 2:
      program[program[pointer + 3]] = program[address1] * program[address2]
      pointer += 4

    elif opcode == 3:
      if len(inputs) == 0:
        return None, -1
      program[address1] = inputs.pop(0)
      pointer += 2

    elif opcode == 4:
      if program[address1] != 0:
        # print("Output value: {}".format(program[address1]))
        return program[address1], pointer+2
      pointer += 2

    elif opcode == 5:
      if program[address1] != 0:
        pointer = program[address2]
      else:
        pointer += 3

    elif opcode == 6:
      if program[address1] == 0:
        pointer = program[address2]
      else:
        pointer += 3

    elif opcode == 7:
      if program[address1] < program[address2]:
        program[program[pointer + 3]] = 1
      else: 
        program[program[pointer + 3]] = 0
      pointer += 4

    elif opcode == 8: 
      if program[address1] == program[address2]:
        program[program[pointer + 3]] = 1
      else:
        program[program[pointer + 3]] = 0
      pointer += 4

  return None, -1

def sequence(s):
  ret = 0
  output = 0

  PRG = {n:l.copy() for n in s}
  PTR = {n:0 for n in s}
  INP = {n:[n] for n in s}
  INP[s[0]].append(0)

  while output is not None:
    for i, n in enumerate(s): 
      output, PTR[n] = intcode(INP[n], PRG[n], PTR[n])
      if output is None:
        return ret
      else:
        ret = output
      
      if i == len(s) - 1:
        INP[s[0]].append(output)
      else:
        INP[s[i+1]].append(output)

ret = 0
for s in permutations(range(5,10)):
  ret = max(ret, sequence(s))

print(ret)