with open('input.txt', 'r') as file:
	lines = file.read().split("\n\n")

patterns = lines[0].strip().split(", ")
towels = lines[1].strip().split("\n")

def count_possible(towel, position):
	if position == len(towel):
		return 1

	s = 0
	for p in [p for p in patterns if towel[position:(position + len(p))] == p]:
		if (p, position) in V:
			s = s + V[(p, position)]
		else:
			V[(p, position)] = count_possible(towel, position+len(p))
			s = s + V[(p, position)]
	return s

ret = 0
for towel in towels:
	V = {}
	ret = ret + count_possible(towel, 0)

print(ret)