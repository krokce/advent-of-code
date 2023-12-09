with open('day09.txt', 'r') as file:
	lines = [list(map(int, l.strip().split(" "))) for l in file.readlines()]

def get_next_1(arr):
	A=[]
	A.append(arr)
	while not all(a == 0 for a in arr):
		tmp = [arr[id]-arr[id-1] for id in range(1, len(arr))]
		A.append(tmp)
		arr = tmp

	next = 0
	for id in range(len(A)-1, -1, -1):
		next = A[id][-1] + next

	return next

def get_next_2(arr):
	A=[]
	A.append(arr)

	while not all(a == 0 for a in arr):
		tmp = [arr[id]-arr[id-1] for id in range(1, len(arr))]
		A.append(tmp)
		arr = tmp

	next = 0
	for id in range(len(A)-1, -1, -1):
		next = A[id][0] - next

	return next

#1
print(sum([get_next_1(l) for l in lines]))

#2
print(sum([get_next_2(l) for l in lines]))