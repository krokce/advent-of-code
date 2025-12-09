from collections import defaultdict

with open('input.txt', 'r') as file:
	lines = [list(map(int, line.strip().split(","))) for line in file]

max_area = 0
for i in range(len(lines)):
	for j in range(i+1, len(lines)):
		area = (max(lines[i][0], lines[j][0])+1 - min(lines[i][0], lines[j][0])) * (max(lines[i][1], lines[j][1])+1 - min(lines[i][1], lines[j][1]))
		max_area = max(max_area, area)

print(max_area) 