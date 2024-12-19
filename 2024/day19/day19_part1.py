import re
with open('input.txt', 'r') as file:
	lines = file.read().split("\n\n")

patterns = lines[0].strip().split(", ")
towels = lines[1].strip().split("\n")

def is_possible(towel):
	visited = set()
	stack = [(len(p), p) for p in patterns if towel[0:len(p)] == p]

	while stack:
		node = stack.pop()
		if node not in visited:
			visited.add(node)
			if node[0] == len(towel):
				return True

			for next in [(node[0]+len(p), p) for p in patterns if towel[node[0]:node[0]+len(p)] == p]:
				if next not in visited:
					stack.append(next)
	return False

cnt = 0
for towel in towels:
	if is_possible(towel):
		cnt = cnt + 1
print(cnt)