with open('day02.txt', 'r') as file:
  input = file.read()

input = [int(i) for i in input.split(",")]
# input = [1,9,10,3,2,3,11,0,99,30,40,50]

def intcode(i, n, v):
  pointer = 0
  input = i.copy()
  input[1] = n
  input[2] = v
  while True or 0 <= pointer < len(input):
    opcode = input[pointer]
    if opcode == 99:
      break
    elif opcode == 1:
      input[input[pointer+3]] = input[input[pointer+ 1]] + input[input[pointer+2]]
      pointer += 4
    elif opcode == 2:
      input[input[pointer+3]] = input[input[pointer+ 1]] * input[input[pointer+2]]
      pointer += 4  
  return input[0]

# 1
print(intcode(input, 12, 2))

# 2
for noun in range(100):
  for verb in range(100):
    if intcode(input, noun, verb) == 19690720:
      print(100*noun+verb)
      break
