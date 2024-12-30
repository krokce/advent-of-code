from collections import defaultdict
from itertools import combinations

with open('input.txt', 'r') as file:
	lines = file.read().strip().split("\n\n")

K = []
L = []

active = None
for k in lines:
	cnt = []
	key_lines = k.split("\n")
	for lid, l in enumerate(key_lines):
		if lid == 0 and l.startswith("#"):
			active = L
			continue
		if lid == 0 and l.startswith("."):
			active = K
			continue
		if lid == len(key_lines)-1:
			continue
		cnt_line = []
		for c in l:
			if c == "#":
				cnt_line.append(1)
			else:
				cnt_line.append(0)
		cnt.append(cnt_line)
	ret = [0,0,0,0,0]
	for i in cnt:
		for jid, j in enumerate(i):
			ret[jid] = ret[jid] + j
	active.append(ret)

def key_fits(key, lock):
	for position in range(len(key)):
		if k[position] + l[position] > 5:
			return False
	return True

ret = 0
for k in K:
	for l in L:
		if key_fits(k, l):
			ret = ret + 1

print(ret)