import heapq 
from collections import defaultdict

with open('input.txt', 'r') as file:
	lines = [list(l.strip()) for l in file.readlines()]

numeric_keypad = {
	# (button position)
	'0':(1,0), 'A':(2,0), '1':(0,1), '2':(1,1), '3':(2,1), '4':(0,2), '5':(1,2), '6':(2,2), '7':(0,3), '8':(1,3), '9':(2,3)
}

directional_keypad = {
	# (button position)
	'<':(0,0),	'v':(1,0),	'>':(2,0), '^':(1,1), 'A':(2,1)
}

directional_keypad_moves = {
	# (arm movement)
	'<':(-1,0),	'v':(0,-1),	'>':(1,0), '^':(0,1), 'A': (0,0)
}

directional_keypad_directions = {
	# (arm movement)
	(-1,0):'<',	(0,-1):'v',	(1,0):'>', (0,1):'^', (0,0): 'A'
}

def find_best_path(keypad_id, start, end):

	if keypad_id == 0:
		keypad = numeric_keypad
	else:
		keypad = directional_keypad

	if start == end:
		return "A"
	
	start_position = keypad[start]
	end_position = keypad[end]

	D = [(-1,0), (0,-1), (1,0), (0,1)]
	Q = []
	V = defaultdict(lambda: float('inf')) 
	P = defaultdict(list)

	heapq.heappush(Q, (0, start_position))
	P[start_position] = [[]]
	
	while Q:
		distance, position = heapq.heappop(Q)

		if position == end_position:
			break

		for did, d in enumerate(D):
			next_x, next_y = position[0] + d[0], position[1] + d[1]

			# not allowed to step out
			if (next_x, next_y) not in keypad.values():
				continue
			
			new_distance = distance + 1

			if new_distance < V[(next_x, next_y)]:
				V[(next_x, next_y)] = new_distance
				heapq.heappush(Q, (new_distance, (next_x, next_y)))
				P[(next_x, next_y)] = [path + [d] for path in P[position]]

			elif new_distance == V[(next_x, next_y)]:
				P[(next_x, next_y)].extend([path + [d] for path in P[position]])
	
	if (sorted(P[end_position][0]) in P[end_position]):
		ret = sorted(P[end_position][0])
	elif (sorted(P[end_position][0], reverse=True) in P[end_position]):
		ret = sorted(P[end_position][0], reverse=True)
	else:
		ret = P[end_position][0]

	return "".join([directional_keypad_directions[s] for s in ret])+"A"

KP = defaultdict(lambda: "A")
S = defaultdict(lambda: float('inf'))

def move(keypad_id, keys, max_keypad_id):

	ret = [""]
	for k in keys:
		from_key = KP[keypad_id]
		to_key = k

		steps = find_best_path(keypad_id, from_key, to_key)
		ret[0] = ret[0] + steps

		KP[keypad_id] = k

	for r in ret:
		S[keypad_id] = min(S[keypad_id], len(r))

	if keypad_id < max_keypad_id:
		for r in ret:
			move(keypad_id+1, r, max_keypad_id)

lvl = 2
ret = 0
for l in lines:
	S = defaultdict(lambda: float('inf'))
	print(l)
	move(0, l, lvl)
	ret = ret + int("".join(l[0:-1])) * S[lvl]

print(ret)
print(S)