import re
with open('input.txt', 'r') as file:
	lines = file.read().split("\n\n")

patterns = lines[0].strip().split(", ")
towels = lines[1].strip().split("\n")

def is_possible_dfs(towel):
	visited = set()
	stack = [(len(p), p) for p in patterns if towel[0:len(p)] == p]
	print(stack)
	ways = 0

	while stack:
		node = stack.pop()
		if node not in visited:
			if node[0] == len(towel):
				visited.add(node)
				ways = ways + 1
				print(ways)

			for next in [(node[0]+len(p), p) for p in patterns if towel[node[0]:node[0]+len(p)] == p]:
				if next not in visited:
					stack.append(next)
	return ways

V = set()

def is_possible(towel, path, ret): 
	if tuple(path) in V:
		return 0
	if len(towel) == 0:
		return 1
	for p in [p for p in patterns if towel[0:len(p)] == p]:
			path.append(p)
			solutions = is_possible(towel[len(p):], path, ret)
			if ret > 0:
				ret = ret + solutions
			else:
				V.add(tuple(path))
				print(V)
	return 0

# cnt = 0
# for towel in towels:
# 	if is_possible_dfs(towel):
# 		print(cnt)
# 		cnt = cnt + 1
# print(cnt)

# print(is_possible("bugwgurruguwwbgwuuggrrbrubgggbgrubbwuuuuuurrgwwurwguwugggg", [], 0))
print(is_possible("brwrr", [], 0))