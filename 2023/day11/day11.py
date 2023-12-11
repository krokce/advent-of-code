import numpy as np

with open('day11.txt', 'r') as file:
	lines = [list(l.strip()) for l in file.readlines()]

data = np.array(lines)

all_dot_rows = np.all(data == '.', axis=1)
index_rows = np.where(all_dot_rows)[0]

all_dot_columns = np.all(data == '.', axis=0)
index_columns = np.where(all_dot_columns)[0]

rows, columns = np.where(data == '#')
pairs = list(zip(rows, columns))

def calc_distance(multiplier):
	ret = 0
	for i in range(len(pairs)):
		for j in range(i+1, len(pairs)):
			cnt_rows = sum([multiplier-1 for id in index_rows if min(pairs[j][0], pairs[i][0]) < id < max(pairs[j][0], pairs[i][0])])
			cnt_cols = sum([multiplier-1 for id in index_columns if min(pairs[j][1], pairs[i][1]) < id < max(pairs[j][1], pairs[i][1])])
			ret += abs(pairs[j][0] - pairs[i][0]) + abs(pairs[j][1] - pairs[i][1]) + cnt_rows + cnt_cols
	return ret

#1
print(calc_distance(2))

#2
print(calc_distance(1_000_000))