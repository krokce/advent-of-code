import re
from collections import defaultdict

with open('day15.txt', 'r') as file:
	init_sequence = file.read().replace("\n", "").split(",")

def hash(str):
	ret = 0
	for s in str:
		ret += ord(s)
		ret *= 17
		ret %= 256
	return ret

#1
ret = 0
for init_step in init_sequence:
	ret += hash(init_step)
print(ret)

#2
BL = defaultdict(list)
BF = defaultdict(list)

def focusig_power():
	ret = 0
	for box_id in range(256):
		for slot_no, focal_length in enumerate(BF[box_id]):
			ret += (box_id + 1) * (slot_no + 1) * int(focal_length)
	return ret

for init_step in init_sequence:
	label, focal_length = re.split(r"[=-]", init_step)
	box = hash(label)
	if label in BL[box]:
		idx = BL[box].index(label)
		if not focal_length:
			del BL[box][idx]
			del BF[box][idx]
		else:
			BF[box][idx] = focal_length
	else:
		if focal_length:
			BL[box].append(label)
			BF[box].append(focal_length)

print(focusig_power())