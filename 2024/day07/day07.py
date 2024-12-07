from itertools import product

with open('input.txt', 'r') as file:
	lines = [(int(a), list(map(int, b.strip().split(" ")))) for a, b in [line.strip().split(":") for line in file]]

operators_1 = ['+', '*']
operators_2 = ['+', '*', '||']

def is_true(result, operands, operators):
	for signs in list(product(operators, repeat=len(operands)-1)):
		a = operands[0]
		for i in range(len(signs)):
			if signs[i] == '*':
				a = a * operands[i+1]
			elif signs[i] == '+':
				a = a + operands[i+1]
			else:
				a = int(str(a) + str(operands[i+1]))
		if a == result:
			return True
	return False

ret1 = 0
ret2 = 0
cnt = 0
for result, operands in lines:
	cnt = cnt + 1
	print(cnt, result, operands)
	if is_true(result, operands, operators_1):
		ret1 = ret1 + result
	else:
		if is_true(result, operands, operators_2):
			ret2 = ret2 + result

# 1
print(ret1)

# 2
print(ret1 + ret2)