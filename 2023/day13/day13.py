from collections import defaultdict

with open('day13.txt', 'r') as file:
	lines = [list(l.strip()) for l in file.readlines()]

P = defaultdict(list)
pattern = []
for lno, l in enumerate(lines):
	if not len(l) or lno == len(lines) - 1:
		P[len(P)] = pattern
		pattern=[]
	else:
		pattern.append(l)

def is_row_mirror(pattern, row, errors):
	err = 0
	max_row, max_col = len(pattern), len(pattern[0])
	if row > max_row:
		return False
	for r_no, r in enumerate(range(row, min(max_row, 2*row))):
		for c in range(0, max_col):
			if pattern[r][c] != pattern[(row-r_no-1)][c]:
				err += 1
				if err > 1:
					return False
	if err == errors:
		return True
	else:
		return False

def is_col_mirror(pattern, col, errors):
	err = 0
	max_row, max_col = len(pattern), len(pattern[0])
	if col > max_col:
		return False
	for c_no, c in enumerate(range(col, min(max_col, 2*col))):
		for r in range(0, max_row):
			if pattern[r][c] != pattern[r][(col-c_no-1)]:
				err += 1
				if err > errors:
					return False
	if err == errors:
		return True
	else:
		return False

#1
ret = 0
for p_no, p in enumerate(P.values()):
	for row in range(1,len(p)):
		if is_row_mirror(p, row, 0):
			ret += 100*row
			break
	for col in range(1,len(p[0])):
		if is_col_mirror(p, col, 0):
			ret += col
			break
print(ret)

#2
ret = 0
for p_no, p in enumerate(P.values()):
	for row in range(1,len(p)):
		if is_row_mirror(p, row, 1):
			ret += 100*row
			break
	for col in range(1,len(p[0])):
		if is_col_mirror(p, col, 1):
			ret += col
			break
print(ret)