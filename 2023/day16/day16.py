from collections import defaultdict

with open('day16.txt', 'r') as file:
	lines = [list(l.strip()) for l in file.readlines()]

max_row = len(lines)
max_col = len(lines[0])

# R, D, L, U
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

turns = {
	"/": {0: [3], 1: [2], 2: [1], 3: [0]},
	"\\": {0: [1], 1: [0], 2: [3], 3: [2]},
	"|": {0: [1,3], 1: [1], 2: [1, 3], 3: [3]},
	"-": {0: [0], 1: [0, 2], 2: [2], 3: [0, 2]},
	".": {0: [0], 1: [1], 2: [2], 3: [3]}
}

def energize(start_position, start_direction):
	beam_position = []
	beam_direction = []
	cell_energized = defaultdict(list)

	beam_position.append(start_position)
	beam_direction.append(start_direction)
	cell_energized[start_position].append(start_direction)

	while len(beam_position) > 0:
		bp = beam_position.pop()
		bd = beam_direction.pop()
		tile_type = lines[bp[0]][bp[1]]
		for next_direction in turns[tile_type][bd]:
			next_row = bp[0] + directions[next_direction][0]
			next_col = bp[1] + directions[next_direction][1]
			if 0 <= next_row < max_row and 0 <= next_col < max_col and next_direction not in cell_energized[(next_row, next_col)]:
				beam_position.append((next_row, next_col))
				beam_direction.append(next_direction)
				cell_energized[(next_row, next_col)].append(next_direction)

	return len(cell_energized)

# 1
print(energize((0,0), 0))

# 2
ret = []

# L, R
for row in range(0, max_row):
	ret.append(energize((row, 0), 0))
	ret.append(energize((row, max_col-1), 2))

# D, U
for col in range(0, max_col):
	ret.append(energize((0, col), 1))
	ret.append(energize((max_row-1, col), 3))

print(max(ret))