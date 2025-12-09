from collections import defaultdict

with open('input.txt', 'r') as file:
	lines = [list(map(int, line.strip().split(","))) for line in file]

lines.append(lines[0])  # close the loop

max_x = max([line[0] for line in lines])
max_y = max([line[1] for line in lines])

PX = defaultdict(set)
PY = defaultdict(set)

start = lines[0]
for i in range(len(lines)):
	if lines[i][0] == start[0]:
		for point in range(min(lines[i][1], start[1]), max(lines[i][1], start[1])+1):
			PX[start[0]].add(point)
	if lines[i][1] == start[1]:
		for point in range(min(lines[i][0], start[0]), max(lines[i][0], start[0])+1):
			PY[start[1]].add(point)
	start = lines[i]

def find_inner_points(arr):
	tmp_arr = []
	arr = sorted(list(arr))
	start = arr[0]
	end = arr[-1]
	current = start
	mode = 1
	for p in arr[1:]:
		if p == end:
			tmp_arr.append((start, end))
		elif p == current + 1:
			current = p
		else:
			if mode == 1:
				current = p
				mode = -1 * mode
			else:
				tmp_arr.append((start, current))
				start = p
				current = p
				mode = -1 * mode

	return tmp_arr

X = defaultdict(list)
for x in range(max_x+1):
	arr = set()
	for py, ls_px in PY.items():
		if x in ls_px:
			arr.add(py)
	
	# arr = arr | set(PX[x])
	if len(arr) > 0:
		X[x]= find_inner_points(arr)

Y = defaultdict(list)
for y in range(max_y+1):
	arr = set()
	for px, ls_py in PX.items():
		if y in ls_py:
			arr.add(px)
	
	# arr = arr | set(PY[y])
	if len(arr) > 0:
		Y[y]= find_inner_points(arr)

def is_rectangle_inside(c1, c2):
	for coord_X in range(c1[0], c2[0]+1):
		res_x1 = False
		res_x2 = False
		if coord_X in X:
			for seg in X[coord_X]:
				if c1[1] >= seg[0] and c1[1] <= seg[1]:
					res_x1 = True
				if c2[1] >= seg[0] and c2[1] <= seg[1]:
					res_x2 = True
			if not res_x1 or not res_x2:
				return False
	
	for coord_Y in range(c1[1], c2[1]+1):
		res_y1 = False
		res_y2 = False		
		if coord_Y in Y:
			for seg in Y[coord_Y]:
				if c1[0] >= seg[0] and c1[0] <= seg[1]:
					res_y1 = True
				if c2[0] >= seg[0] and c2[0] <= seg[1]:
					res_y2 = True
			if not res_y1 or not res_y2:
				return False

	return True

max_area = 0
for i in range(len(lines)):
	for j in range(i+1, len(lines)):
		corner_1 = (min(lines[i][0], lines[j][0]), min(lines[i][1], lines[j][1]))
		corner_2 = (max(lines[i][0], lines[j][0]), max(lines[i][1], lines[j][1]))
		area = (corner_2[0] + 1 - corner_1[0]) * (corner_2[1] + 1 - corner_1[1])
		if area > max_area and is_rectangle_inside(corner_1, corner_2):
			max_area = area
			print("Max rectangle area:", area, "Corners:", corner_1, corner_2)

print(max_area) 