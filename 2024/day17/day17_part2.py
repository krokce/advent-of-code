import re
from copy import deepcopy

with open('input.txt', 'r') as file:
	lines = file.read().split("\n\n")

registers = list(map(int, re.findall(r'\d+', lines[0])))
program = list(map(int, re.findall(r'\d+', lines[1])))
# print(registers, program)

# for l in lines:
# 	re.findall("\d+")

# print(lines)

def literal(operand):
	return operand

def combo(registers, operand):
	if 0 <= operand <= 3:
		return operand
	if operand == 4:
		return registers[0]
	if operand == 5:
		return registers[1]
	if operand == 6:
		return registers[2]

def run(registers, program, pointer, output):
	opcode = program[pointer]
	operand = program[pointer+1]
	instruction = ''
	if opcode == 0:
		instruction = 'adv'
		registers[0] = int(registers[0] / pow(2, combo(registers, operand)))
		return pointer+2
	if opcode == 1:
		instruction = 'bxl'
		registers[1] = registers[1] ^ literal(operand)
		return pointer+2
	if opcode == 2:
		instruction = 'bst'
		registers[1] = combo(registers, operand) % 8
		return pointer+2
	if opcode == 3:
		instruction = 'jnz'
		if registers[0] != 0:
			pointer = literal(operand)
			return pointer
		else:
			return pointer+2
	if opcode == 4:
		instruction = 'bxc'
		registers[1] = registers[1] ^ registers[2]
		return pointer+2
	if opcode == 5:
		instruction = 'out'
		output.append(combo(registers, operand) % 8)
		return pointer+2
	if opcode == 6:
		instruction = 'bdv'
		registers[1] = int(registers[0] / pow(2, combo(registers, operand)))
		return pointer+2
	if opcode == 7:
		instruction = 'cdv'
		registers[2] = int(registers[0] / pow(2, combo(registers, operand)))
		return pointer+2

output = []

def exec(reg):
	step = 1
	output = []
	p = 0
	while True:
		p = run(reg, program, p, output)
		step = step + 1
		if p >= len(program)-1:
			return(int(''.join(map(str, output))))

my_program = int(''.join(map(str, program)))

for reg in range(164541017976456, 264541017976456):
	my_regs = [reg, 0, 0]
	res = exec(my_regs)
	if my_program == res:
		print(my_program)
		print(res)
		print("=", reg)
		break