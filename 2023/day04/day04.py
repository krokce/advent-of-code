import re
from collections import defaultdict

with open('day04.txt', 'r') as file:
	lines = [l.strip().split(':') for l in file.readlines()]

def count_wins(card_id):
	winning_numbers, have_numbers = lines[card_id-1][1].split('|')
	winning_numbers = re.findall(r'\d+', winning_numbers)
	have_numbers = re.findall(r'\d+', have_numbers)	
	return sum([1 for n in have_numbers if n in winning_numbers])

#2 hold counts of scratchcards copies in possession (inital one of each)
cards = {i:1 for i in range(1, len(lines)+1)}

ret = 0
for card_id in cards.keys():
	wins = count_wins(card_id)
	
	#1 calculate score for each card
	ret += pow(2, wins-1) if wins>0 else 0

	#2 handle counts of scratchcards copies I won
	for c_id in range(card_id+1, card_id+1+wins):
		cards[c_id] += cards[card_id]

#1
print(ret)

#2
print(sum(cards.values()))