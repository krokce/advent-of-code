from collections import defaultdict

with open('input.txt', 'r') as file:
	lines = [l.strip().split("-") for l in file.readlines()]

M = defaultdict(set)

S = []
for c1, c2 in lines:
	M[c1].add(c2)
	M[c2].add(c1)
	S.append({c1, c2})

for m, mcon in M.items():
	for s in S:
		if len(mcon & s) == len(s):
			s.add(m)

print(",".join(sorted(list(sorted(zip([len(a) for a in S], S),reverse=True)[0][1]))))