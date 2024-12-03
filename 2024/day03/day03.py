import re
with open('input.txt', 'r') as file:
	line = file.read()

# 1
m = re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", line)

ret = 0
for pair in m:
	ret = ret + int(pair[0]) * int(pair[1])

print(ret)

# 2
m = re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)|(don't\(\))|(do\(\))", line)

ret = 0
mode = 1
for pair in m:
	if "do()" in pair:
		mode = 1
		continue
	if "don't()" in pair:
		mode = 0
		continue
	ret = ret + int(pair[0]) * int(pair[1]) * mode

print(ret)