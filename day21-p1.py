import re

with open('day21.txt', 'r') as file:
  lines = file.read().strip().split("\n")

position = {}
for l in lines:
  r = re.findall(r"\d+", l)
  position[int(r[0])] = int(r[1])

dice = 1
player = 1
player_score = {1:0, 2:0}
roll_count = 0
while True:
  roll_count += 1
  dice_value = sum(range(dice, dice+3))
  new_position = (position[player] + dice_value - 1) % 10 + 1
  player_score[player] += new_position
  position[player] = new_position
  if player_score[player] >= 1000: 
    print(player_score[player % 2 + 1] * roll_count * 3)
    break
  dice += 3
  if dice > 100:
    dice = dice % 100
  player = player % 2 + 1