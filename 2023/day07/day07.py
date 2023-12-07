import math
from collections import defaultdict

with open('day07.txt', 'r') as file:
	lines = [l.strip().split(' ') for l in file.readlines()]

hands = []
for hand, bet in lines:
	hands.append((hand, int(bet)))

def find_key_by_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None

def hand_strength_1(hand):
	card_strength = list(reversed(['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']))
	h = defaultdict(int)

	# card strength
	ret = 0
	for cid, c in enumerate(hand):
		h[c] += 1
		ret += (card_strength.index(c)+1) * pow(100, 5-cid)

	# add type strength
	ret1 = 0
	for cnt in h.values():
		ret1 += pow(cnt, 2)
	ret1 += ret1 * math.pow(10, 13)

	return ret + ret1

def hand_strength_2(hand):
	card_strength = list(reversed(['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']))
	h = defaultdict(int)

	# card strength
	ret = 0
	for cid, c in enumerate(hand):
		h[c] += 1
		ret += (card_strength.index(c)+1) * pow(100, 5-cid)

	# deal with Joker cards
	if 'J' in h:
		cnt_jokers = h['J']
		del h['J']	
		for cnt in range(5, 0, -1):
			# all jokers !!!
			if len(h) == 0:
				h['J'] = 5
			elif cnt in h.values():
				h[find_key_by_value(h, cnt)] += cnt_jokers
				break

	# add type strength
	ret1 = 0
	for cnt in h.values():
		ret1 += pow(cnt, 2)
	ret1 += ret1*math.pow(10, 13)

	return ret + ret1

#1
ret = 0
for id, (hand, bet) in enumerate(sorted(hands, key=lambda hand:hand_strength_1(hand[0]))):
	ret += (id+1) * bet
print(ret)

#2
ret = 0
for id, (hand, bet) in enumerate(sorted(hands, key=lambda hand:hand_strength_2(hand[0]))):
	ret += (id+1) * bet
print(ret)
