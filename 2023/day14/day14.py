with open('day14.txt', 'r') as file:
	lines = [list(l.strip()) for l in file.readlines()]

# N, E, S, W
directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def flip_lever(map, d):
	max_row, max_col = len(map), len(map[0])

	from_row = max_row-1 if d == 2 else 0
	to_row = -1 if d == 2 else max_row

	from_col = max_col-1 if d == 3 else 0
	to_col = -1 if d == 3 else max_col

	row_step = -1 if d == 2 else 1
	col_step = -1 if d == 3 else 1

	for row in range(from_row, to_row, row_step):
		for col in range(from_col, to_col, col_step):
			if map[row][col] == 'O':
				next_row, next_col = row, col
				while True:
					if max_row > next_row + directions[d][0] >= 0 and max_col > next_col + directions[d][1] >= 0 and map[next_row + directions[d][0]][next_col + directions[d][1]] == '.':
						next_row, next_col = next_row + directions[d][0], next_col + directions[d][1]
					else:
						break
				if row != next_row or col != next_col:
					map[row][col] = '.'
					map[next_row][next_col] = 'O'

	return map

def print_map(map):
	max_row, max_col = len(map), len(map[0])
	for row in range(max_row):
		for col in range(max_col):
			print(map[row][col], end='')
		print()
	print()

def get_load(map):
	max_row, max_col = len(map), len(map[0])
	ret = 0
	for row in range(max_row):
		for col in range(max_col):
			if map[row][col] == 'O':
				ret += max_row-row
	return ret

def spin_cycle(map):
	for d in range(4):
		map = flip_lever(map, d)
	return map

def get_map_hash(map):
	max_row, max_col = len(map), len(map[0])
	ret = []
	for row in range(max_row):
		for col in range(max_col):
			if map[row][col] == 'O':
				ret.append((row,col))
	return tuple(ret)

#1
map = lines.copy()
map = flip_lever(map, 0)
print(get_load(map))

#2
map = lines.copy()
seen_maps = []
seeen_loads = []
for cycle_no in range(1_000_000_000):
	map = spin_cycle(map)
	map_hash = get_map_hash(map)
	if map_hash in seen_maps:
		seen_idx = seen_maps.index(map_hash)
		delta = cycle_no-seen_idx
		print(seeen_loads[seen_idx + (1_000_000_000-seen_idx-1) % delta])
		break
	seen_maps.append(map_hash)
	seeen_loads.append(get_load(map))