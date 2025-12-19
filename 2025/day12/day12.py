import math 

with open('input.txt', 'r') as file:
	lines = [line.strip().split(": ") for line in file.readlines() if line.find('x') > -1]

ret = 0
for bag, shapes in lines:
	bag = list(map(int, bag.split("x")))
	shapes = list(map(int, shapes.split()))
	if (math.prod(bag) > sum(shapes) * 7):
		ret = ret + 1

print(ret)