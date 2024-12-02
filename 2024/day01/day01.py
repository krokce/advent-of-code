with open('input.txt', 'r') as file:
	lines = [map(int, l.strip().split())  for l in file.readlines()]

list1, list2 = list(zip(*lines))

list1 = sorted(list1)
list2 = sorted(list2)

ret = 0
for i in range(len(list1)):
	ret = ret + abs(list1[i] - list2[i])

# 1
print(ret)

ret = 0
for i in range(len(list1)):
	ret = ret + list1[i] * list2.count(list1[i])

# 2
print(ret)