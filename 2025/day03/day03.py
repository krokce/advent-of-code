with open('input.txt', 'r') as file:
	lines = [l.strip() for l in file.readlines()]

def get_joltage(bank, battery_positions):
	ret = 0
	for digit, pos in enumerate(battery_positions):
		ret = ret + int(bank[pos]) * pow(10, len(battery_positions) - digit - 1)
	return ret

def get_max(bank, bat_count):
	battery_positions = []

	# intitialize battery positions
	for b in range(bat_count):
		battery_positions.append(len(bank) - bat_count + b)
	
	# get initial joltage
	max_joltage = get_joltage(bank, battery_positions)
	max_positions = battery_positions.copy()

	for b in range(bat_count):
		position_from = int(battery_positions[b])-1
		position_to = int(battery_positions[b-1])+1 if b > 0 else 0
		for pos in range(position_from, position_to-1, -1):
			battery_positions[b] = pos
			joltage = get_joltage(bank, battery_positions)
			if joltage >= max_joltage:
				max_joltage = joltage
				max_positions = battery_positions.copy()
		battery_positions = max_positions.copy()
	return max_joltage

ret1 = 0
ret2 = 0
for bank in lines:
	ret1 = ret1 + get_max(bank, 2)
	ret2 = ret2 + get_max(bank, 12)

print(ret1)
print(ret2)