import sys
sys.setrecursionlimit(100000)

with open('day18.txt', 'r') as file:
	lines = [l.strip().split(" ") for l in file.readlines()]

# R, D, L, U
directions = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}

T = {}
position = (0, 0)

for direction, steps, color  in lines:
	for i in range(int(steps)):
		position = (position[0] + directions[direction][0], position[1] + directions[direction][1])
		T[position] = color.replace('(','').replace(')', '')

def fill(position):
	for d in directions.values():
		new_position = (position[0] + d[0], position[1] + d[1])
		if new_position not in T:
			T[new_position] = 1
			fill(new_position)

fill((1,1))

#1
print(len(T))