from collections import defaultdict

with open('input.txt', 'r') as file:
	lines = file.read().split("\n\n")

M = defaultdict(set)
init = {x: int(y) for x, y in [str.split(":") for str in lines[0].strip().split("\n")]}
ops = [l.split() for l in lines[1].strip().split("\n")]

def do_op(o):
	if o[1] == "OR":
		init[o[4]] = init[o[0]] or init[o[2]]
	if o[1] == "AND":
		init[o[4]] = init[o[0]] and init[o[2]]
	if o[1] == "XOR":
		init[o[4]] = init[o[0]] ^ init[o[2]]

while ops:
	for oid, o in enumerate(ops):
		if o[0] in init and o[2] in init:
			do_op(ops.pop(oid))

print(int("".join([str(v) for k, v in sorted(init.items(), reverse=True) if k.startswith("z")]), 2))