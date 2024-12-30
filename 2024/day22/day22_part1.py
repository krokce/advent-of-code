with open('input.txt', 'r') as file:
	lines = [int(l.strip()) for l in file.readlines()]

def new_secret(num):
	a = num * 64
	ret = num ^ a
	ret = ret % 16777216
	b = int(ret / 32)
	ret = ret ^ b
	ret = ret %  16777216
	c = ret * 2048
	ret = ret ^ c
	ret = ret %  16777216
	return ret

def get_nth_secret(num, n):
	ret = num
	for i in range(n):
		ret = new_secret(ret)
	return ret

ret = 0
for l in lines:
	ret = ret + get_nth_secret(l, 2000)

print(ret)