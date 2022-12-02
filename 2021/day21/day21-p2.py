import re
import itertools

with open('day21.txt', 'r') as file:
  lines = file.read().strip().split("\n")

position = {}
for l in lines:
  r = re.findall(r"\d+", l)
  position[int(r[0])] = int(r[1])

W = {}
def game(p1_position, p1_score, p2_position, p2_score, turn):

  if (p1_position, p1_score, p2_position, p2_score, turn) in W:
    return W[(p1_position, p1_score, p2_position, p2_score, turn)]

  if p1_score >= 21:
    return(1, 0)
  
  if p2_score >= 21:
    return(0, 1)

  p1_wins = 0
  p2_wins = 0
  for dices in itertools.product((1,2,3),(1,2,3),(1,2,3)):
    if turn == 1:
      new_p1_position = (p1_position + sum(dices) - 1) % 10 + 1
      new_p1_score = p1_score + new_p1_position
      wp1, wp2 = game(new_p1_position, new_p1_score, p2_position, p2_score, 2)
    else:
      new_p2_position = (p2_position + sum(dices) - 1) % 10 + 1
      new_p2_score = p2_score + new_p2_position
      wp1, wp2 = game(p1_position, p1_score, new_p2_position, new_p2_score, 1)
    p1_wins += wp1
    p2_wins += wp2

  W[(p1_position, p1_score, p2_position, p2_score, turn)] = (p1_wins, p2_wins)
  return (p1_wins, p2_wins)

print(max(game(position[1], 0, position[2], 0, 1)))