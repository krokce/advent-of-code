from collections import defaultdict

with open('input.txt', 'r') as file:
	S = {int(k):1 for k in file.readline().split()}

def blink(S):
	R = defaultdict(int)
	for k, i in [(k, i) for k, i in S.items()]:
		if k == 0:
			R[1] = R[1] + i
		elif len(str(k))%2 == 0:
			left = int(str(k)[:len(str(k))//2])
			right = int(str(k)[len(str(k))//2:])
			R[left] = R[left] + i
			R[right] = R[right] + i
		else:
			R[k*2024] = R[k*2024] + i
	return R

for b in range(75):
	# 1
	if b == 25:
		print(sum([v for v in S.values()]))
	S = blink(S)

# 2
print(sum([v for v in S.values()]))